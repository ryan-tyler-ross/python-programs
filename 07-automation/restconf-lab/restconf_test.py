"""Read a RESTCONF resource using lab settings from the environment."""

import os

import requests


def main():
    url = os.environ.get("RESTCONF_URL")
    username = os.environ.get("RESTCONF_USERNAME")
    password = os.environ.get("RESTCONF_PASSWORD")
    if not all((url, username, password)):
        raise SystemExit("Set RESTCONF_URL, RESTCONF_USERNAME, and RESTCONF_PASSWORD first.")
    try:
        response = requests.get(
            url,
            auth=(username, password),
            headers={"Accept": "application/yang-data+json"},
            timeout=(5, 15),
        )
        response.raise_for_status()
        print(response.json())
    except (requests.RequestException, ValueError) as error:
        raise SystemExit(f"RESTCONF request failed: {error}") from error


if __name__ == "__main__":
    main()
