# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320,
    "AMZN": 140
}

total_investment = 0
portfolio = []

n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
        portfolio.append([stock, quantity, investment])
        print(f"Investment in {stock}: ${investment}")
    else:
        print("Stock not found!")

print("\n----- Portfolio Summary -----")
for item in portfolio:
    print(f"{item[0]} : {item[1]} shares = ${item[2]}")

print(f"\nTotal Investment = ${total_investment}")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-------------------------\n")

    for item in portfolio:
        file.write(f"{item[0]} : {item[1]} shares = ${item[2]}\n")

    file.write(f"\nTotal Investment = ${total_investment}")

print("\nPortfolio saved to portfolio.txt")