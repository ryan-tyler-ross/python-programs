"""Wait longer between failed GET requests, with a little random jitter."""

import random
import time
import argparse
import os

import requests

RETRYABLE = {500, 502, 503, 504}


def fetch(url, headers, attempts=5):
    for attempt in range(attempts):
        try:
            response = requests.get(url, headers=headers, timeout=(5, 10))
        except (requests.ConnectionError, requests.Timeout):
            if attempt == attempts - 1:
                raise
        else:
            if response.status_code not in RETRYABLE or attempt == attempts - 1:
                response.raise_for_status()
                return response.json()
        delay = min(2 ** attempt, 16) + random.uniform(0, 0.5)
        print(f"Attempt {attempt + 1} failed; retrying in {delay:.1f} seconds.")
        time.sleep(delay)
    raise RuntimeError("No attempts were made")

def main():
    parser = argparse.ArgumentParser(description="Retry temporary failures with increasing delays.")
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
