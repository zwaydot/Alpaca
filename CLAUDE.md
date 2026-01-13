# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Alpaca trading project for developing and testing trading strategies using the Alpaca Trading API. The project defaults to paper trading (simulation) mode for safe testing.

## Setup

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys (copy from example and edit)
cp .env.example .env
# Edit .env with your Alpaca credentials
```

## API Endpoints

- **Paper Trading**: `https://paper-api.alpaca.markets/v2`
- **Live Trading**: `https://api.alpaca.markets/v2`

Set `ALPACA_PAPER_TRADE` in `.env` to switch between modes.

## Common Tasks

**Get account info:**
```bash
python -c "from strategy_template import get_account; print(get_account())"
```

**Run a strategy:**
```bash
python your_strategy.py
```
