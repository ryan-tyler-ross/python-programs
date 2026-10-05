class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Collect valid coin counts; return False if input is invalid."""
        print("Please insert coins.")
        self.money_received = 0
        try:
            for coin, value in self.COIN_VALUES.items():
                count = int(input(f"How many {coin}?: "))
                if count < 0:
                    raise ValueError("Coin counts cannot be negative")
                self.money_received += count * round(value * 100)
        except ValueError:
            print("Enter nonnegative whole numbers. Money refunded.")
            self.money_received = 0
            return False
        self.money_received /= 100
        return True

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        if not self.process_coins():
            return False
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
