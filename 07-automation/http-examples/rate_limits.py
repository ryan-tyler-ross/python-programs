"""Honor Retry-After on HTTP 429, then retry the GET once."""

import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import argparse
import os

import requests


def retry_delay(value):
    if value is None:
        return 60
    try:
        return max(0, int(value))
    except ValueError:
        try:
            deadline = parsedate_to_datetime(value)
            if deadline.tzinfo is None:
                deadline = deadline.replace(tzinfo=timezone.utc)
            return max(0, (deadline - datetime.now(timezone.utc)).total_seconds())
        except (TypeError, ValueError, OverflowError):
            return 60


def fetch(url, headers):
    response = requests.get(url, headers=headers, timeout=(5, 10))
    if response.status_code == 429:
        delay = retry_delay(response.headers.get("Retry-After"))
        print(f"Rate limited; waiting {delay:.1f} seconds before one retry.")
        time.sleep(delay)
        response = requests.get(url, headers=headers, timeout=(5, 10))
    response.raise_for_status()
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="Wait after a rate limit and retry once.")
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
