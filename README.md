# Alpaca Trading Project

Trading strategies and tools for Alpaca API.

## Setup

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Set up your Alpaca API credentials in `.env`:

```
ALPACA_API_KEY=your_api_key
ALPACA_SECRET_KEY=your_secret_key
ALPACA_PAPER_TRADE=True
```

## Usage

Run your trading scripts:

```bash
python your_strategy.py
```
