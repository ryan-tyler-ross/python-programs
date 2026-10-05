"""A simplified card game: the dealer draws until reaching 17."""

import random


def get_card():
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])


def total_score(hand):
    score = sum(hand)
    # Each ace may count as 1 instead of 11; never change the original hand.
    for card in hand:
        if card == 11 and score > 21:
            score -= 10
    return score


def outcome(player, dealer):
    if player > 21:
        return "You went over 21. You lose!"
    if dealer > 21:
        return "Dealer went over 21. You win!"
    if player == dealer:
        return "Draw!"
    return "You win!" if player > dealer else "You lose!"


def play():
    player = [get_card(), get_card()]
    dealer = [get_card(), get_card()]
    print(f"Dealer's first card: {dealer[0]}")
    while total_score(player) < 21:
        print(f"Your cards: {player}; score: {total_score(player)}")
        choice = input("Draw or stand? ").strip().lower()
        if choice == "stand":
            break
        if choice != "draw":
            print("Please enter draw or stand.")
            continue
        player.append(get_card())
    if total_score(player) <= 21:
        while total_score(dealer) < 17:
            dealer.append(get_card())
    print(f"Your cards: {player}; score: {total_score(player)}")
    print(f"Dealer's cards: {dealer}; score: {total_score(dealer)}")
    print(outcome(total_score(player), total_score(dealer)))


if __name__ == "__main__":
    play()
