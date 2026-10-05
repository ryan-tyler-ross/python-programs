"""Set separate connection and read timeouts on a GET request."""

import argparse
import os

import requests


def fetch(url, headers):
    response = requests.get(url, headers=headers, timeout=(5, 15))
    response.raise_for_status()
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="Fetch JSON with connection and read timeouts.")
    parser.add_argument("url", help="URL of your lab API")
    args = parser.parse_args()
    headers = {}
    token = os.environ.get("API_TOKEN")
    if token:
        headers["Auth-Token"] = token
    try:
        print(fetch(args.url, headers))
    except (requests.RequestException, ValueError, RuntimeError) as error:
        parser.exit(1, f"Request failed: {error}\n")


if __name__ == "__main__":
    main()
