"""Combine a city and pet name into a suggested band name."""


def main():
    city = input("What was the name of the city you grew up in?\n")
    pets_name = input("What is the name of your pet?\n")
    band_name = city + " " + pets_name
    print("Your band name could be " + band_name)


if __name__ == "__main__":
    main()
