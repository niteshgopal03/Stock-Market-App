import time
import requests
from config import TIMEOUT, MAX_RETRIES

def Safe_request(url, params):
    for attempt in range(MAX_RETRIES):
        response = requests.get(url, params=params, timeout=TIMEOUT)

        if response.status_code == 200:
            return response.json()

        time.sleep(2 ** attempt)

    return {}
