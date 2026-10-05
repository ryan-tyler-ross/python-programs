# Pomodoro timer

[pomodoro.py](pomodoro.py) cycles through four 25-minute focus sessions, 5-minute
short breaks, and a 20-minute long break. Pause/resume preserves the time remaining;
a monotonic deadline drives the countdown.

Entry: `python3 desktop/pomodoro-timer/pomodoro.py`.
Dependency: [Pillow](requirements.txt), plus a graphical desktop with Tk support.
Linux sound alerts use `canberra-gtk-play` and a desktop sound theme.
[sisyphus_unbothered.jpg](sisyphus_unbothered.jpg) is the bundled background.

At each transition the window stays on top until a click, keypress, or 15-second timeout.
The Beep button plays the alert sound.
