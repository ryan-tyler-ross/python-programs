from turtle import Turtle, Screen
import random


def main():
    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
    y_position = [-70, -40, -10, 20, 50, 80]
    all_turtles = []

    user_bet = screen.textinput(title="Make your bet!",
                                prompt="Which turtle will win the race? "
                                       "Enter a color (Red, Blue,Green, Yellow, Cyan, Magenta: ")
    if user_bet:
        user_bet = user_bet.strip().lower()
        while user_bet not in colors:
            user_bet = screen.textinput("Choose a color", ", ".join(colors))
            if user_bet is None:
                break
            user_bet = user_bet.strip().lower()
        is_race_on = user_bet in colors

    for turtle_index in range(0, 6):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(-230, y_position[turtle_index])
        all_turtles.append(new_turtle)

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You win! The {winning_color} turtle wins!")
                else:
                    print(f"You lost! The {winning_color} turtle wins!")
                break
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

    screen.exitonclick()


if __name__ == "__main__":
    main()
