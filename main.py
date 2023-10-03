ticker = "AAPL"
opening_price = 142.7
closing_price = 143.2
volume = 1200000
print(ticker, opening_price, closing_price, volume)
ticker = "LVMH"
opening_price = 1721.2
closing_price = 1724.4
volume = 1300000
print(ticker, opening_price, closing_price, volume)

string = "currencypair"
string = "buyingrate"
string = "sellingrate"
currencypair = "EUR/USD"
buyingrate = 1,1825
sellingrate = 1,1830

stocks = ["AAPL", "MSFT", "GOOGL"]
stocks.append("IBM")
print(stocks)

stocks = "TSLA", "AMZN", "FB", "NVDA", "AMD"
print(stocks)
# Create a dictionary to store stock details
stock_details = {
    "Ticker": "AAPL",
    "Opening Price": 142.7,
    "Closing Price": 143.2,
    "Volume": 1200000
}
print(stock_details)
bond_details = {
    "Issuer": "FED",
    "Maturity Date": 2030,
    "Coupon Rate": "5%",
    "Face Value": 1000
}
print(bond_details)

stock_prices = [100, 101, 102, 98, 97]
for i in range(1, len(stock_prices)):
    daily_return = (stock_prices[i] - stock_prices[i-1]) / stock_prices[i-1]
    print(daily_return)

principal = 1000
rate = 0.05
years = 0

while principal < 2000:
    principal *= (1 + rate)
    years += 1

print("It takes", years, "years for the principal to reach $2000.")

stock_prices = [105, 107, 104, 106, 103]

for i in range(1, len(stock_prices)):
    daily_return = (stock_prices[i] - stock_prices[i-1]) / stock_prices[i-1]
    print(daily_return)
    average_return = sum(daily_return) / len(daily_return)

    print("Average Return:", average_return)

# Initial principal amount
principal = 500

rate = 0.07

# Initialize the number of years
years = 0

# Continue looping until the principal reaches or exceeds $1000
while principal < 1000:
    # Compound the principal by multiplying it by (1 + rate)
    principal *= (1 + rate)

    # Increment the number of years
    years += 1

# Print the number of years it takes to reach $1000
print("It takes", years, "years to reach $1000.")


