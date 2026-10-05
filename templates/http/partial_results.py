"""Keep successful results when one of several APIs fails."""

import argparse
import logging
import os

import requests


def fetch(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=(5, 10))
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as error:
        logging.warning("Skipping %s: %s", url, error)
        return None


def main():
    parser = argparse.ArgumentParser(description="Collect JSON from several lab URLs.")
    parser.add_argument("urls", nargs="+", help="URLs to fetch independently")
    args = parser.parse_args()
    headers = {}
    token = os.environ.get("API_TOKEN")
    if token:
        headers["Auth-Token"] = token
    results = {url: fetch(url, headers) for url in args.urls}
    successful = {url: result for url, result in results.items() if result is not None}
    failed = [url for url, result in results.items() if result is None]
    print("Results:", successful)
    print(f"Collected {len(successful)} URLs. Skipped: {failed}")


if __name__ == "__main__":
    main()
