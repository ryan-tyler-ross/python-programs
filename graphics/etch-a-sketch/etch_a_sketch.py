"""Draw with keyboard callbacks: W/S move, A/D turn, and C clears."""

from turtle import Screen, Turtle


def main():
    screen = Screen()
    pen = Turtle()

    def clear_and_center():
        pen.clear()
        pen.penup()
        pen.home()
        pen.pendown()

    screen.listen()
    screen.onkey(lambda: pen.forward(10), "w")
    screen.onkey(lambda: pen.backward(10), "s")
    screen.onkey(lambda: pen.left(10), "a")
    screen.onkey(lambda: pen.right(10), "d")
    screen.onkey(clear_and_center, "c")
    screen.exitonclick()


if __name__ == "__main__":
    main()
