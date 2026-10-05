#!/usr/bin/env python3
"""Pomodoro timer for the Linux desktop.

Cycles through four 25-minute focus blocks separated by short breaks and
closed out by a long one. At every transition the window is pinned above
whatever else is on screen and an alert sample is played.

Two platform details drive the design, both verified on Fedora/KDE with
Wayland (Tk runs through XWayland, it has no native Wayland backend):

* Raising the window only works while ``-topmost`` stays set. Switching it
  on and straight back off never sets ``_NET_WM_STATE_ABOVE``, so KWin has
  nothing to act on and the window does not move.
* Python 3.14 ships no standard-library audio playback -- ``winsound`` is
  Windows-only and PEP 594 removed ``ossaudiodev`` and ``audioop``. The
  alert therefore hands off to ``canberra-gtk-play``, part of the desktop's
  own sound stack, rather than pulling in a third-party audio package.
"""

import math
import os
import subprocess
import time
import tkinter as tk

from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# (label, minutes) in the order they run, looping back round at the end.
SESSIONS = (
    ("Focus 1/4", 25), ("Short Break", 5),
    ("Focus 2/4", 25), ("Short Break", 5),
    ("Focus 3/4", 25), ("Short Break", 5),
    ("Focus 4/4", 25), ("Long Break", 20),
)

# Event name from the freedesktop sound theme in /usr/share/sounds.
ALERT_SOUND = "alarm-clock-elapsed"

# How long the window stays pinned on top if nobody acknowledges it. Without
# this a missed alert leaves the window above every other app indefinitely.
ALERT_HOLD_MS = 15_000

# The countdown is driven off a monotonic deadline, so this only controls how
# promptly the display catches up, never how long a session actually lasts.
# Four wake-ups a second is free next to the cost of running the event loop,
# and it stops the visible clock from skipping or repeating a second.
TICK_MS = 250

WINDOW_SIZE = 400


class PomodoroTimer:
    """Tk application that walks through ``SESSIONS`` on a wall-clock deadline."""

    def __init__(self, root):
        self.root = root
        self.index = 0
        self.running = True
        self.tick_id = None
        self.sound = None

        # Seconds left in the current session, and the monotonic timestamp it
        # ends at. Deriving the display from a deadline rather than counting
        # decrements means a slow or delayed callback cannot stretch a session.
        self.remaining = SESSIONS[0][1] * 60
        self.deadline = time.monotonic() + self.remaining

        self._build_ui()

        # Any interaction is treated as acknowledging the alert. Bindings on the
        # toplevel also catch events on its children, so the buttons count too.
        self.root.bind("<Button-1>", self.clear_alert)
        self.root.bind("<Key>", self.clear_alert)

        self.tick()

    def _build_ui(self):
        """Lay out the background image and the three foreground widgets."""
        self.root.title("Pomodoro Timer")
        self.root.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}")

        # Pillow is required because Tk cannot decode JPEG on its own. The
        # reference is kept on the instance or the image would be collected.
        image = Image.open(os.path.join(BASE_DIR, "sisyphus_unbothered.jpg"))
        self.photo = ImageTk.PhotoImage(image.resize((WINDOW_SIZE, WINDOW_SIZE)))
        tk.Label(self.root, image=self.photo).place(x=0, y=0)

        self.status_label = tk.Label(
            self.root, text=SESSIONS[0][0],
            font=("Arial", 16, "bold"), bg="black", fg="#deaa88",
        )
        self.status_label.place(relx=0.5, rely=0.63, anchor="center")

        self.counter_label = tk.Label(
            self.root, text="",
            font=("Arial", 26, "bold"), bg="black", fg="white",
        )
        self.counter_label.place(relx=0.5, rely=0.74, anchor="center")

        self.pause_button = tk.Button(
            self.root, text="Pause", font=("Arial", 12, "bold"),
            command=self.toggle_pause,
            bg="white", fg="black", padx=10, pady=5,
        )
        self.pause_button.place(relx=0.35, rely=0.88, anchor="center")

        # Handy for checking the alert is audible without waiting out a session.
        tk.Button(
            self.root, text="Beep", font=("Arial", 12, "bold"),
            command=self.play_sound,
            bg="white", fg="black", padx=10, pady=5,
        ).place(relx=0.65, rely=0.88, anchor="center")

    def tick(self):
        """Refresh the clock, then either reschedule or roll over."""
        if not self.running:
            return

        self.remaining = self.deadline - time.monotonic()
        if self.remaining <= 0:
            self.next_session()
            return

        # Round up so a fresh session reads 25:00 rather than 24:59.
        seconds = math.ceil(self.remaining)
        self.counter_label.config(text=f"{seconds // 60:02}:{seconds % 60:02}")
        self.tick_id = self.root.after(TICK_MS, self.tick)

    def next_session(self):
        """Fire the alert and start the following block."""
        self.trigger_alert()
        self.index = (self.index + 1) % len(SESSIONS)

        label, minutes = SESSIONS[self.index]
        self.remaining = minutes * 60
        self.deadline = time.monotonic() + self.remaining
        self.status_label.config(text=label)
        self.tick()

    def toggle_pause(self):
        """Stop or resume the countdown, holding the remaining time across it."""
        self.running = not self.running

        if self.running:
            # Rebuild the deadline from whatever was left when we stopped.
            self.deadline = time.monotonic() + self.remaining
            self.pause_button.config(text="Pause")
            self.tick()
            return

        self.pause_button.config(text="Resume")
        # Cancel the pending callback, otherwise resuming would leave two tick
        # chains running and the clock would count down at double speed.
        if self.tick_id is not None:
            self.root.after_cancel(self.tick_id)
            self.tick_id = None

    def trigger_alert(self):
        """Pin the window above everything else and sound the alert."""
        self.root.deiconify()  # in case it was minimised
        self.root.attributes("-topmost", True)
        self.root.lift()
        self.root.focus_force()
        self.root.after(ALERT_HOLD_MS, self.clear_alert)
        self.play_sound()

    def clear_alert(self, event=None):
        """Release the always-on-top state set by :meth:`trigger_alert`."""
        self.root.attributes("-topmost", False)

    def play_sound(self):
        """Start the alert sample without stalling the event loop.

        ``subprocess.run`` would block until playback finished, freezing the
        countdown for the length of the sample. The poll() check reaps the
        previous player and keeps repeated presses from stacking up.
        """
        if self.sound is not None and self.sound.poll() is None:
            return
        self.sound = subprocess.Popen(
            ("canberra-gtk-play", "-i", ALERT_SOUND),
            stderr=subprocess.DEVNULL,
        )


def main():
    root = tk.Tk()
    PomodoroTimer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
