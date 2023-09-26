import numpy as np
import pandas as pd
import numpy_financial as npf
cash_flows = np.array([-100000, 20000, 25000, 30000, 35000, 40000])
discount_rate = 0.1

# Calculate NPV
npv = np.sum(cash_flows / (1 + discount_rate) ** np.arange(len(cash_flows)))

print("Net Present Value:", npv)
irr = npf.irr(cash_flows)

print("Internal Rate of Return:", irr)
principal = 10000  # initial amount of money
rate = 0.05  # interest rate
time = 5  # time in years
simple_interest = principal * rate * time
print("Simple Interest:", simple_interest)
compound_interest = principal * ((1 + rate) ** time - 1)
print("Compound Interest:", compound_interest)
import pandas as pd

# Sample price data
prices = pd.Series([1, 3, 7, 9, 12, 14, 16, 19, 23, 26])

# Calculating 3-day simple moving average
moving_average = prices.rolling(window=3).mean()

# Print the moving average
print("Moving Average:\n", moving_average)
weights = np.array([0.4, 0.6])  # for two assets in the portfolio
returns = np.array([0.1, 0.12])  # expected returns of the assets
cov_matrix = np.array([[0.1, 0.03], [0.03, 0.12]])  # covariance matrix

# Calculate the portfolio variance
portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))

print("Portfolio Variance:", portfolio_variance)
