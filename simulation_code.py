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
        / historical_data['Open']
        * 3
)

historical_data['net_Change'] = 1 + historical_data['PC_Change']

# if there is a 5% change instead of doing (100*.05) + 100 we just do 100 * 1.05
# so if we have an series of 5%, 2%, -1%, -5% the values in the series is 1.05, 1.02, -.99, -.95 and then we can just multiply all of these values together 1.05 * 1.02 * -.99 * -.95 * 100 to see the cumulative percent change on 100$

# Extracting Open and Close prices
price_changes = historical_data['net_Change'].to_numpy()

#simulated days
num_series = 1000000
num_draws = 1000

simulations = np.zeros((num_series, num_draws))

for series_i in range(num_series):
    random_draws = np.random.choice(price_changes, size=num_draws, replace=True)
    simulations[series_i] = random_draws
    
np.save("simulations", simulations)

row_products = np.prod(simulations, axis = 1)
row_products = (row_products - 1) * 100
print(row_products.max())



# to simulate doubling down your investment:
# Function to simulate the effect on investment
def simulate_investment(initial_investment, percent_changes, doubling_down_threshold):
    investment = initial_investment
    values = [investment]
    #double_down_count = 0
    for percent_change in percent_changes:
        investment *= percent_change

        if percent_change < 1 + doubling_down_threshold:
            # Double down on the investment
            investment += initial_investment
            #double_down_count += 1

        values.append(investment)

    return values

# Parameters
initial_investment = 100
doubling_down_threshold = -0.2  #threshold for doubling down on losses

# Simulate the effect on investment for each series
simulated_investments = []
for series in simulations:
    simulated_values = simulate_investment(initial_investment, series, doubling_down_threshold)
    simulated_investments.append(simulated_values)
