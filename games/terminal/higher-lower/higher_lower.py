from game_data import data
from art import logo, vs
import random


def format_data(answer):
    answer_name = answer['name']
    answer_description = answer['description']
    answer_country = answer['country']
    return f"{answer_name}, {answer_description} from {answer_country}"


def get_winning_answer(ans_a, ans_b):
    if ans_a['follower_count'] > ans_b['follower_count']:
        return ans_a
    else:
        return ans_b


def player_selects(answer_a, answer_b):
    ask = input("Who has more followers? A or B: ").strip().lower()
    while ask not in ("a", "b"):
        ask = input("Please enter A or B: ").strip().lower()
    return answer_a if ask == "a" else answer_b


def score_round(player_answer, correct_answer):
    return player_answer == correct_answer


def main():
    print(logo)
    game_continues = True
    answer_b = random.choice(data)
    score = 0

    while game_continues:

        answer_a = answer_b

        while answer_a == answer_b or answer_a['follower_count'] == answer_b['follower_count']:
            answer_b = random.choice(data)

        print(f"Compare A: {format_data(answer_a)}")
        print(vs)
        print(f"Compare B: {format_data(answer_b)}")

        winning_answer = get_winning_answer(answer_a, answer_b)
        player_choice = player_selects(answer_a, answer_b)
        is_correct = score_round(player_choice, winning_answer)

        if is_correct:
            score += 1
            print("\n"*100)
            print(logo)
            print(f"Your current score is {score}")
        else:
            print(f"\nIncorrect! Your final score is {score}. Play again soon!")
            game_continues = False


if __name__ == "__main__":
    main()
