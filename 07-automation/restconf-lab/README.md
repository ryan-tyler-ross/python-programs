# RESTCONF lab

Read a JSON resource from a device in your own lab.

From the course root: `python 07-automation/restconf-lab/restconf_test.py`.

Requires requests. Copy `.env.example` to `.env` and fill in your endpoint, username, and password. From this folder, load settings with `set -a; source .env; set +a`, then run the script. TLS verification stays enabled; the endpoint must have a trusted certificate. The moved `.venv` is local tooling; its launchers now use this folder's path.

- `restconf_test.py` — Make a read-only GET using an explicit RESTCONF URL and HTTP basic authentication.
- `requirements.txt` — Standalone requests dependency for this lab.
- `.env.example` — Template for the endpoint and credentials; copy and fill it locally.
- `.env` — Local settings file moved from AUTOCOR; initially empty and ignored by Git.
- `.gitignore` — Keep .env and the local virtual environment out of Git.
