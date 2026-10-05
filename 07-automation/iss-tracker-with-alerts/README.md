# ISS alerts

Read two public APIs and print an alert when the ISS is near Area 51 at night.

From the course root: `python 07-automation/iss-tracker-with-alerts/main.py`.

Requires requests and internet access. Stop with Ctrl+C. Email is optional: set sender/recipient in send_alert(), set GMAIL_APP_PASSWORD, and enable the commented call. Printing alerts is the default.

- `main.py` — Poll ISS position and UTC sun times once a minute; print an alert for a nighttime pass.
