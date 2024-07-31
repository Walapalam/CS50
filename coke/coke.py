amount_due = 50
change = 0

denominations = [25, 10, 5]

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    coin = int(input("Insert Coin: "))

    if coin in denominations:
        amount_due -= coin

change = abs(amount_due)
print(f"Change Owed: {change}")