"""Simulate orders, coin payments, and ingredient stock with dictionaries."""

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

INITIAL_RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def pull_ingredients(resource, drink):
    for ingredient, amount in drink["ingredients"].items():
        resource[ingredient] -= amount
    return resource


def check_resources(resource, drink):
    for ingredient, amount in drink["ingredients"].items():
        if resource.get(ingredient, 0) < amount:
            return False
    return True


def process_coins(resource, drink):
    """Accept payment before using any ingredients."""
    drink_cost = drink["cost"]
    print("Please insert coins.")
    try:
        customer_payment = 0
        for coin, value in {"quarters": 25, "dimes": 10, "nickels": 5, "pennies": 1}.items():
            count = int(input(f"How many {coin}? "))
            if count < 0:
                raise ValueError("Coin counts cannot be negative")
            customer_payment += count * value
        customer_payment /= 100
    except ValueError:
        print("Invalid input. Please enter numbers only. Money refunded.")
        return resource

    if customer_payment >= drink_cost:
        change_required = round(customer_payment - drink_cost, 2)
        resource["money"] += drink_cost
        pull_ingredients(resource, drink)
        if change_required > 0:
            print(f"Here's your drink! Your change is ${change_required}.")
        else:
            print("Here's your drink!")
    else:
        print("Sorry, that's not enough money. Money refunded.")
    return resource


def main():
    resources = INITIAL_RESOURCES.copy()
    input_errors = 0

    while input_errors < 5:
        selection = input("Order espresso/latte/cappuccino, report, or off: ").strip().lower()

        if selection == "off":
            break

        elif selection == "report":
            for key, value in resources.items():
                print(key, value)

        elif selection in MENU:
            available = check_resources(resources, MENU[selection])
            if available:
                process_coins(resources, MENU[selection])
            else:
                print("Sorry, that drink is not currently available.")
        else:
            print("Sorry, that's not a valid option.")
            input_errors += 1


if __name__ == "__main__":
    main()
