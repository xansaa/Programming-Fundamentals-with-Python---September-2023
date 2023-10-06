def total_price(name, quantity):
    price = 0
    if name == "coffee":
        price = quantity * 1.5
    elif name == "water":
        price = quantity * 1
    elif name == "coke":
        price = quantity * 1.4
    elif name == "snacks":
        price = quantity * 2
    return price

product = input()
numbers = int(input())
price = total_price(product, numbers)
print(f"{price:.2f}")