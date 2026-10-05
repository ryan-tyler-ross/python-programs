# HTTP examples

Each short script teaches one failure-handling pattern and can run on its own.

Requires requests. From this folder: python timeouts.py https://your-lab.example/api. Replace the URL with your own endpoint. API_TOKEN is optional and becomes the Auth-Token header. partial_results.py accepts multiple URLs. Retries apply to GET requests; permanent errors stop immediately.

- `timeouts.py` — Make one GET with separate connection and read timeouts.
- `server_errors.py` — Retry connection failures and HTTP 500/502/503/504 up to three total attempts.
- `backoff.py` — Retry those temporary failures up to five times, with increasing waits and jitter.
- `rate_limits.py` — Honor Retry-After seconds or an HTTP date on 429, then retry once.
- `partial_results.py` — Fetch several URLs independently and retain successful results.
