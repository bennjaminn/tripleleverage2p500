import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Set the ticker symbol for the S&P 500
ticker_symbol = "^GSPC"

# # Calculate the date 10 years ago from today
# ten_years_ago = datetime.now() - timedelta(days=10 * 365)

# Create a yfinance Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch historical data
historical_data = ticker.history(
    period='max',
    interval="1d",
)


historical_data['PC_Change'] = (historical_data['Close'] - historical_data['Open']) / historical_data['Open'] * 100

historical_data['PC_Change'].to_csv('SP500_daily_pc_change.csv', index=False)

# historical_data.to_csv('SP500_daily')
