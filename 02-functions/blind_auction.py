"""Collect bids in a dictionary and find the highest bidder."""


def find_highest_bidder(bids):
    winner = max(bids, key=bids.get)
    return winner, bids[winner]


def main():
    bids = {}
    while True:
        name = input("Bidder name: ").strip()
        if not name or name in bids:
            print("Enter a new, nonempty bidder name.")
            continue
        try:
            bid = int(input("Bid in whole dollars: $"))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if bid < 0:
            print("Bids must be nonnegative.")
            continue
        bids[name] = bid
        more = input("Any more bidders? (yes/no): ").strip().lower()
        while more not in ("yes", "no"):
            more = input("Please enter yes or no: ").strip().lower()
        if more == "no":
            break
        print("\n" * 20)
    winner, amount = find_highest_bidder(bids)
    print(f"The winner is {winner} with a bid of ${amount}.")


if __name__ == "__main__":
    main()
