MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        report_storage()
        welcome_order()
    elif user_input == "off":
        return
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
    print(f"${profit}")


def calculate_money():
    """Calculate and returns total of amount paid"""
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    return quarters + dimes + nickles + pennies


def pay_for_order(order):
    """Processes the order after payment"""
    money_paid = calculate_money()

    if money_paid < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        welcome_order()

    for key, value in resources.items():
        if value < MENU[order]["ingredients"][key]:
            print(f"Sorry, there isn't enough {key}")
            welcome_order()

    serve_order(order, money_paid)
    update_resources(order)
    welcome_order()


def serve_order(coffe_order, amount):
    """Takes order and amount as input and serves order"""
    profit += amount
    change = amount - MENU[coffe_order]["cost"]
    print(f"Here is ${round(change, 2)} in change")
    print(f"Here is your {coffe_order}. Enjoy!")


def update_resources(coffe_order):
    """Updates the quantities in resources after order"""
    resources["water"] -= MENU[coffe_order]["ingredients"]["water"]
    resources["milk"] -= MENU[coffe_order]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffe_order]["ingredients"]["coffee"]


welcome_order()
