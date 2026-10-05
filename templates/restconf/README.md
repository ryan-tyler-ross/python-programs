# RESTCONF request template

[get_resource.py](get_resource.py) reads a JSON resource using HTTP basic
authentication, explicit timeouts, and TLS certificate verification.

Dependency: [requests](requirements.txt). Entry:
`python3 templates/restconf/get_resource.py`.

Configuration: `RESTCONF_URL`, `RESTCONF_USERNAME`, and `RESTCONF_PASSWORD` in the
process environment. [.env.example](.env.example) records the setting names with a
placeholder endpoint. A local `.env` is ignored and must be loaded into the environment
before running; the script does not load it automatically.
