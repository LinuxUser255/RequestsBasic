import requests
from requests.exceptions import RequestException

KRAKEN_URL = "https://api.kraken.com/0/public/Ticker"
params = {"pair": "XBTCUSD"}


def get_btc_price(url: str = KRAKEN_URL) -> float | None:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()["result"]["XXBTZUSD"]["c"][0]
    except RequestException as e:
        print(f"Request failed: {e}")
        return None


