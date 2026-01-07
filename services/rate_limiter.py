import time
import requests

TIMEOUT = 15
MAX_RETRIES = 3
RETRY_DELAY = 3

def Safe_request(url, params):
    for attempt in range(MAX_RETRIES):
        response = requests.get(url, params=params, timeout=TIMEOUT)

        if response.status_code == 200:
            return response.json()

        time.sleep(2 ** attempt)

    return {}
