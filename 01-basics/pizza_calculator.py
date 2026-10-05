"""Add toppings to a pizza's base price."""

print("Python Pizza: small $15, medium $20, large $25; cheese $1.")
size = input("Size (small/medium/large): ").strip().lower()
while size not in ("small", "medium", "large"):
    size = input("Please choose small, medium, or large: ").strip().lower()

pepperoni = input("Pepperoni (yes/no): ").strip().lower()
while pepperoni not in ("yes", "no"):
    pepperoni = input("Please enter yes or no: ").strip().lower()

cheese = input("Extra cheese (yes/no): ").strip().lower()
while cheese not in ("yes", "no"):
    cheese = input("Please enter yes or no: ").strip().lower()

if size == "small":
    total = 15
elif size == "medium":
    total = 20
else:
    total = 25

if pepperoni == "yes":
    total += 2 if size == "small" else 3
if cheese == "yes":
    total += 1

print(f"Your total is ${total:.2f}. Enjoy your pizza!")
