"""Use list indexes and conditions to play one round."""

import random

moves = ["rock", "paper", "scissors"]
choice = input("Type 1 for rock, 2 for paper, or 3 for scissors: ").strip()
while choice not in ("1", "2", "3"):
    choice = input("Please enter 1, 2, or 3: ").strip()

player = int(choice) - 1
computer = random.randrange(3)
print(f"You chose {moves[player]}. Computer chose {moves[computer]}.")

if player == computer:
    print("Draw!")
elif (player == 0 and computer == 2
      or player == 1 and computer == 0
      or player == 2 and computer == 1):
    print("You win!")
else:
    print("You lose!")
