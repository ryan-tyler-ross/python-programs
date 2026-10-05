"""Shift letters around the alphabet; keep spaces and punctuation."""

import string


def caesar_cipher(text, shift):
    result = ""
    for letter in text:
        if letter in string.ascii_lowercase:
            position = string.ascii_lowercase.index(letter)
            result += string.ascii_lowercase[(position + shift) % 26]
        else:
            result += letter
    return result


def main():
    direction = input("Encode or decode? ").strip().lower()
    while direction not in ("encode", "decode"):
        direction = input("Please enter encode or decode: ").strip().lower()
    text = input("Message: ").lower()
    while True:
        try:
            shift = int(input("Shift number: "))
            break
        except ValueError:
            print("Please enter a whole number.")
    if direction == "decode":
        shift = -shift
    print(caesar_cipher(text, shift))


if __name__ == "__main__":
    main()
