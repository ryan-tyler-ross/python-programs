import pandas
import turtle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def main():
    data = pandas.read_csv(BASE_DIR / "50_states.csv")
    image = str(BASE_DIR / "blank_states_img.gif")
    # screen settings
    screen = turtle.Screen()
    screen.title("US States Game")
    screen.addshape(image)
    screen.setup(760, 520)
    turtle.shape(image)

    guessed_states = []
    all_states = data.state.values.tolist()
    while len(guessed_states) < len(all_states):
        answer = screen.textinput(title=f"{len(guessed_states)}/50 states",
                                  prompt="Name a state, or type Exit to quit")
        answer_state = answer.strip().title() if answer else "Exit"

        if answer_state == "Exit":
            missing = [s for s in all_states if s not in guessed_states]
            pandas.DataFrame(missing, columns=["state"]).to_csv(BASE_DIR / "missing_states.csv", index=False)
            break
        if answer_state in all_states and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state, align="center", font =("Arial", 7, "normal"))

    turtle.mainloop()


if __name__ == "__main__":
    main()
