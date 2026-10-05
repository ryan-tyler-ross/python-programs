"""Calculate with named functions, then optionally reuse the result."""


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    return first / second


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def main():
    first = read_number("First number: ")
    while True:
        operator = input("Operation (+, -, *, /): ").strip()
        if operator not in OPERATIONS:
            print("Choose one of +, -, *, /.")
            continue
        second = read_number("Second number: ")
        if operator == "/" and second == 0:
            print("Cannot divide by zero.")
            continue
        result = OPERATIONS[operator](first, second)
        print(f"{first} {operator} {second} = {result}")
        action = input("Continue with result, start new, or quit? (continue/new/quit): ").strip().lower()
        while action not in ("continue", "new", "quit"):
            action = input("Please enter continue, new, or quit: ").strip().lower()
        if action == "quit":
            return
        first = result if action == "continue" else read_number("First number: ")


if __name__ == "__main__":
    main()
