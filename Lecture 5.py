import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Understanding DataFrame Class

opening_prices = [105.00, 100.00, 102.00]
volumes = [1000.00, 1050.00, 1200.00]

date_range = pd.date_range(start='2021-01-04', periods=3, freq='D')

df1 = pd.DataFrame({'Opening Price': opening_prices, 'Volume': volumes}, index=date_range)

print("Exercise 1")
print(df1)

high = [107, 102.55, 104.40]
low = [103.70, 99.00, 100.50]

df2 = pd.DataFrame({'Opening Price': opening_prices, 'Volume': volumes, 'High': high, 'Low': low}, index=date_range)

print("Exercise 2")
print(df2)

closing_prices = np.array([106, 99.80, 103.5, 110, 108.65, 94.70, 100.80])
df3 = pd.DataFrame({'Closing Price': closing_prices})

df3['Price Change'] = df3['Closing Price'].pct_change() * 100

print("Exercise 3")
print(df3)

volumes_trade = np.array([10000, 12000, 9000, 11000, 10000])
average_trade = np.array([200, 220, 420, 270, 370])

df4 = pd.DataFrame({'Volume': volumes_trade, 'Average Trade Size': average_trade})

print("Exercise 4")
print(df4)

date_index = pd.date_range(start='2023-01-01', end='2023-01-31', freq='B')  # 'B' frequency stands for business days

closing_prices = np.random.uniform(100, 150, size=len(date_index))
trading_volume = np.random.randint(50000, 100000, size=len(date_index))

df5 = pd.DataFrame({'Date': date_index, 'Close': closing_prices, 'Volume': trading_volume})

mondays = df5[df5['Date'].dt.weekday == 0]

average_volume_mondays = mondays['Volume'].mean()

print('Exercise 5')
print("One month of trading data:")
print(df5)

print("Mondays:")
print(mondays)

print("Average Volume Mondays:", average_volume_mondays)

weekday = df5['Date'].dt.day_name()
df6 = df5.copy()
df6['Day of the week'] = weekday

# df6['Magical Level'] = np.random.randint(1, 10, size=len(df6))
print('Exercise 6')
print(df6)

# Basic Analytics with Pandas

date_range = pd.date_range(start='2023-11-11', periods=8, freq='B')

closing_prices2 = np.random.uniform(100, 150, size=len(date_range))

df7 = pd.DataFrame({'Date': date_range, 'Close': closing_prices2})

mean_price = df7['Close'].mean()
median_price = df7['Close'].median()

print('Exercise 1')
print(df7)
print('Mean', mean_price)
print('Median', median_price)

max_price = df7['Close'].max()
min_price = df7['Close'].min()
day_highest_price = df7.loc[df7['Close'].idxmax()]['Date']
day_lowest_price = df7.loc[df7['Close'].idxmin()]['Date']


print('Exercise 2')
print('Max price', max_price, 'Min price', min_price)
print('Highest Price', day_highest_price, 'Lowest Price', day_lowest_price)

# Basic Visualization with Pandas

df7['Close'].plot(title='Stock Closing Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.show()
