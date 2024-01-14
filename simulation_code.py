import numpy as np
import matplotlib.pyplot as plt
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

# Extracting Open and Close prices
open_close_prices = historical_data[['Open', 'Close']]

print(open_close_prices)


#simulated days
num_series = 1000
num_draws = 1000

df = pd.DataFrame()

for series_id in range(num_series):
    random_draws = np.random.choice(sp500_data['Percent_Change'], size = num_draws, replace = True)
    series_name = f'Series_{series_id + 1}'
    df[series_name] = random_draws
