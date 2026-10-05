"""Split a bill, including its tip, among a group."""


def main():
    print("Welcome to the tip calculator!")
    try:
        bill = float(input("Total bill: $"))
        tip = float(input("Tip percentage: "))
        people = int(input("Number of people: "))
        if bill < 0 or tip < 0 or people <= 0:
            print("Bill and tip must be nonnegative; people must be greater than zero.")
        else:
            per_person = bill * (1 + tip / 100) / people
            print(f"Each person should pay ${per_person:.2f}")
    except ValueError:
        print("Enter numbers for the bill and tip, and a whole number for people.")


if __name__ == "__main__":
    main()
