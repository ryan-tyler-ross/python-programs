from turtle import Turtle, Screen

pen = Turtle()


screen = Screen()

def move_forward():
    Lily.forward(10)
def move_backward():
    Lily.backward(10)
def move_counter_clockwise():
    Lily.left(10)
def move_clockwise():
    Lily.right(10)
def clear_and_center():
    Lily.goto(0, 0)
    Lily.clear()
    Lily.setheading(0)

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = move_counter_clockwise)
screen.onkey(key = "d", fun = move_clockwise)
screen.onkey(key = "c", fun = clear_and_center)
screen.exitonclick()
