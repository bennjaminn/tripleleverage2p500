import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Set the ticker symbol for the S&P 500
ticker_symbol = "^GSPC"

# Calculate the date 10 years ago from today
ten_years_ago = datetime.now() - timedelta(days=10 * 365)

# Create a yfinance Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch historical data
historical_data = ticker.history(
    start=ten_years_ago.strftime('%Y-%m-%d'),
    interval="1d"
)

historical_data['PC_Change'] = (
    (historical_data['Close'] - historical_data['Open'])
    / historical_data['Open'] * 3
)

# Extracting Open and Close prices
pc_changes = historical_data['PC_Change'].to_numpy()

#simulated days
num_series = 1000
num_draws = 1000

simulations = np.zeros((num_draws, num_series))

for series_i in range(num_series):
    random_draws = np.random.choice(pc_changes, size=num_draws, replace=True)
    simulations[series_i] = random_draws

