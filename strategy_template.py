"""Alpaca trading strategy template."""
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
PAPER_TRADE = os.getenv("ALPACA_PAPER_TRADE", "True").lower() == "true"

BASE_URL = (
    "https://paper-api.alpaca.markets"
    if PAPER_TRADE
    else "https://api.alpaca.markets"
)

HEADERS = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY,
}


def get_account():
    """Get account information."""
    response = requests.get(f"{BASE_URL}/v2/account", headers=HEADERS)
    return response.json()


if __name__ == "__main__":
    account = get_account()
    print(f"Account: {account}")
