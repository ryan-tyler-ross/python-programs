# ISS tracker

[main.py](main.py) polls ISS position and sunrise/sunset APIs once a minute.
The example location is Area 51, a public coordinate. Sun times refresh once a day;
one console alert is printed per nearby nighttime pass.

Dependency: [requests](requirements.txt). Entry:
`python3 automation/iss-tracker/main.py`. Stop with Ctrl+C.

Optional email uses `send_alert()`: set its placeholder sender and recipient locally,
provide `GMAIL_APP_PASSWORD` in the environment, and enable the call in the polling loop.
