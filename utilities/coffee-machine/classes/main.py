"""Use three small classes to take coffee orders."""

from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker


def main():
    menu = Menu()
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()

    while True:
        choice = input(f"Order ({menu.get_items()}), report, or off: ").strip().lower()
        if choice == "off":
            return
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
            continue
        drink = menu.find_drink(choice)
        if drink is None:
            continue
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
