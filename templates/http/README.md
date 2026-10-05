# HTTP request templates

Independent GET examples with explicit timeouts and JSON responses. Each file
contains its own request function and command-line entry point.

| File | Pattern |
| --- | --- |
| [timeouts.py](timeouts.py) | Separate connection and read timeouts. |
| [server_errors.py](server_errors.py) | Up to three attempts for connection failures or HTTP 500/502/503/504. |
| [backoff.py](backoff.py) | Up to five attempts with increasing delays and jitter. |
| [rate_limits.py](rate_limits.py) | One retry after HTTP 429, honoring seconds or a date in `Retry-After`. |
| [partial_results.py](partial_results.py) | Fetch several URLs independently and retain successful results. |

Dependency: [requests](requirements.txt). Entry example:
`python3 templates/http/timeouts.py https://api.example.com/resource`.
`partial_results.py` accepts multiple URLs. Optional `API_TOKEN` supplies the
`Auth-Token` header; adapt that header to the target API. Permanent errors stop retries.
