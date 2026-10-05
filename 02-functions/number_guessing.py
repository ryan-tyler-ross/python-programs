"""Guess a secret number before the attempts run out."""

import random


def play():
    answer = random.randint(1, 100)
    difficulty = input("Difficulty (easy/hard): ").strip().lower()
    while difficulty not in ("easy", "hard"):
        difficulty = input("Please enter easy or hard: ").strip().lower()
    attempts = 10 if difficulty == "easy" else 5

    while attempts > 0:
        print(f"You have {attempts} guesses left.")
        try:
            guess = int(input("Guess a number from 1 to 100: "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if not 1 <= guess <= 100:
            print("Choose a number from 1 to 100.")
            continue
        if guess == answer:
            print(f"You win! The number was {answer}.")
            return
        print("Too high." if guess > answer else "Too low.")
        attempts -= 1
    print(f"Out of guesses. The number was {answer}.")


if __name__ == "__main__":
    play()
