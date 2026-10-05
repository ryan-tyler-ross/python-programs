"""Draw a grid of dots using a fixed palette sampled from the painting."""

import random
from turtle import Screen, Turtle

COLORS = [(148, 91, 59), (56, 33, 20), (173, 148, 53),
          (42, 103, 153), (31, 40, 57), (127, 170, 191), (221, 207, 121)]


def main():
    screen = Screen()
    screen.colormode(255)
    pen = Turtle()
    pen.hideturtle()
    pen.penup()
    pen.speed("fastest")

    for row in range(10):
        for column in range(10):
            pen.goto(-180 + column * 40, -180 + row * 40)
            pen.dot(20, random.choice(COLORS))

    screen.exitonclick()


if __name__ == "__main__":
    main()
