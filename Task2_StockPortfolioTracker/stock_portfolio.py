import csv

# Hardcoded stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145,
}

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks and prices:")
for name, price in stock_prices.items():
    print(" ", name, "- $" + str(price))

portfolio = {}  # stock name -> quantity

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Sorry, that stock is not in the list. Please try again.")
        continue

    quantity_text = input("Enter quantity of " + stock + ": ").strip()

    if not quantity_text.isdigit() or int(quantity_text) == 0:
        print("Please enter a whole number greater than 0.")
        continue

    quantity = int(quantity_text)

    # If the stock was already added, add to the existing quantity
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print("Added", quantity, "shares of", stock)

if len(portfolio) == 0:
    print("\nNo stocks entered. Goodbye!")
else:
    print("\n----- Your Portfolio -----")
    total_investment = 0
    rows = []

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_investment = total_investment + value
        rows.append([stock, quantity, price, value])
        print(stock, ":", quantity, "x $" + str(price), "= $" + str(value))

    print("--------------------------")
    print("Total investment value: $" + str(total_investment))

    save = input("\nSave the result to a file? (yes/no): ").lower().strip()

    if save == "yes" or save == "y":
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            writer.writerows(rows)
            writer.writerow(["Total", "", "", total_investment])
        print("Saved to portfolio.csv")
    else:
        print("Not saved. Goodbye!")
