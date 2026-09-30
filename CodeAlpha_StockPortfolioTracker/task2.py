stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 400,
    "GOOGL": 150
}

total_investment = 0

print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock}: ${investment}")

print(f"\nTotal Investment: ${total_investment}")

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: ${total_investment}\n")

print("Result saved to portfolio.txt")