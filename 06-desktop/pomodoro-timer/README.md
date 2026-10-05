# Pomodoro timer

A Linux desktop timer with pause/resume, a background image, and transition alerts.

From the course root: `python 06-desktop/pomodoro-timer/pomodoro.py`.

Requires Pillow, Tk support, canberra-gtk-play, and a desktop sound theme. The alert stays on top until a click, keypress, or 15-second timeout. The monotonic deadline avoids clock drift; sound runs in a separate process so the timer stays responsive.

- `pomodoro.py` — Run four 25-minute focus sessions with short and long breaks, pause, and alerts.
- `sisyphus_unbothered.jpg` — Background image loaded by the timer.
