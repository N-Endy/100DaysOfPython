print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

size_price = {'S': 15, 'M': 20, 'L': 25}
price = 0

for item in size_price:
    if item == size:
        price = size_price[item]

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1

print(f"The total amount for your pizza is ${price}")