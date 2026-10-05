"""Draw overlapping circles, rotating three degrees after each one."""

import random
import turtle


def main():
    turtle.colormode(255)
    turtle.speed("fastest")

    for angle in range(0, 360, 3):
        turtle.color(tuple(random.randint(0, 255) for _ in range(3)))
        turtle.setheading(angle)
        turtle.circle(100)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
