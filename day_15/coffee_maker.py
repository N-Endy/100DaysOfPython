MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print out initial offerings
# note coffee ordered for
# calculate correctly coffee fee
# give change with order
# report
# switch off machine


def welcome_order():
    """Request input for an order or action"""
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        report_storage()
        welcome_order()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        pay_for_order(user_input)
    else:
        welcome_order()


def report_storage():
    """Prints the storage left of coffee resources"""
    for key, value in resources.items():
        key = key.capitalize()
        if key == "Water" or key == "Milk":
            print(f"{key}: {value}ml")
        else:
            print(f"{key}: {value}g")


def calculate_money():
    """Calculate and returns total of amount paid"""
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    penny = 0.01
    quarters = int(input("How many quarters?: ")) * quarter
    dimes = int(input("How many dimes?: ")) * dime
    nickles = int(input("How many nickles?: ")) * nickle
    pennies = int(input("How many pennies?: ")) * penny

    return quarters + dimes + nickles + pennies


def pay_for_order(order):
    money_paid = calculate_money()

    if money_paid < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        welcome_order()

    for key, value in resources.items():
        if value < MENU[order]["ingredients"][key]:
            print(f"Sorry, there isn't enough {key}")
            welcome_order()


welcome_order()
