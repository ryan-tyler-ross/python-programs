"""Track guessed letters and remaining lives in a word game."""

import random

from hangman_art import stages
from hangman_words import word_list


def play():
    word = random.choice(word_list)
    guesses = []
    lives = 6
    print("Let's play Hangman!")
    while lives > 0:
        display = "".join(letter if letter in guesses else "_" for letter in word)
        print(display, stages[lives])
        if "_" not in display:
            print("You win!")
            return
        guess = input("Guess one letter: ").strip().lower()
        if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
            print("Enter one letter from a to z.")
            continue
        if guess in guesses:
            print("You already guessed that letter.")
            continue
        guesses.append(guess)
        if guess not in word:
            lives -= 1
        print("Guesses:", ", ".join(guesses))
    print(stages[0])
    print(f"You lose! The word was {word}.")


if __name__ == "__main__":
    play()
