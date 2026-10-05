"""A single-file Snake game with movement, food, scoring, and collisions."""

from turtle import Turtle, Screen
import random
import time

# For Snake Class #
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
# For Scoreboard Class #
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 12, "bold")
TOXIC_SNAKE_FRIEND = ["Ur better than that.", "Are u proud of that score?", "Someone needs coffee...",
                     "Ur fired.", "*fart*", "Watch where you crawl!", "Skill issue?", "Dont start crying...",
                     "Im telling your boss.", "*yawn*", "That was... neat.", "U shld see an eye doctor.",
                     "R u fo real...?", "Hope no one saw that.", "I thought u wanted to play?",
                     "*vomit*", "U shld uninstall...", "*rain noises*", "*slow fart*", "Back to work, you.",
                     "Plz don't go...", "But we just started...", "Quitters never win...",
                     "See you soon.", "*cackle*", "shh... sleep now...",
                     "Why not give up?", "Seek help."]

class Snake:
    """ Creates the Snake """
    def __init__(self):
        """ create the snake object """
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        """ create the snake segments, add to the snake body, and position at center """
        x = 0
        for _ in range(0, 3):
            starting_segment = Turtle("square")
            starting_segment.color("white")
            starting_segment.penup()
            starting_segment.goto(x, 0)
            self.snake_body.append(starting_segment)
            x -= 20

    def grow(self):
        """ adds a new snake segment to the body of the snake """
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(self.snake_body[-1].xcor(), self.snake_body[-1].ycor())
        self.snake_body.append(segment)

    def move(self):
        """ moves the snake from back to front to keep the snake together """
        for segment_number in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_number - 1].xcor()
            new_y = self.snake_body[segment_number - 1].ycor()
            self.snake_body[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """ moves the snake upwards unless it's going downwards """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        """ moves the snake left """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """ moves the snake downwards """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """ moves the snake right """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

class Food(Turtle):
    """ Creates the Food """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-280, 281, MOVE_DISTANCE)
        random_y = random.randrange(-280, 261, MOVE_DISTANCE)
        self.goto(random_x, random_y)

class Scoreboard(Turtle):
    """ Creates the Scoreboard"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 270)
        self.write(f"Score = {self.score} ", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("green")
        self.write(f"GAME OVER. {random.choice(TOXIC_SNAKE_FRIEND)}", True, align=ALIGNMENT, font=GAME_OVER_FONT)

    def watch_walls(self):
        self.goto(0, -50)
        self.color("green")
        self.write("Watch out for walls.", True, align=ALIGNMENT, font=GAME_OVER_FONT)

    def watch_yourself(self):
        self.goto(0, -50)
        self.color("green")
        self.write("You ran into yourself.", True, align=ALIGNMENT, font=GAME_OVER_FONT)


def main():
    # ________________ Main Program______________ #
    # game difficulty settings (screen refresh rate)
    insane_mode = 0.05
    standard_game = 0.1

    # create and set up the screen with the desired size, color, and title
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("SNEK! For when you need to take a brek.")
    screen.tracer(0)

    # sets the 'speed' of the screen refresh via prompt window and player input
    level_select = screen.textinput(title= "Difficulty Select",
                                    prompt= "You can try 'insane' or get a standard game.\n"
                                            "Use the arrow keys to move the Snake.\n"
                                            "Press OK to continue.\n")
    level_select = (level_select or "").strip().lower()
    if level_select == "insane":
        speed = insane_mode
    else:
        speed = standard_game

    # create and display the scoreboard
    scoreboard = Scoreboard()

    # create the snake object
    snek = Snake()

    # create the food object
    nomnom = Food()

    # pressing an arrow key calls a method that changes the direction of the snake head
    screen.listen()
    screen.onkey(snek.up, "Up")
    screen.onkey(snek.down, "Down")
    screen.onkey(snek.left, "Left")
    screen.onkey(snek.right, "Right")

    # while the game is running, the snake is moving
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(speed)
        snek.move()

        # detect collision with food and grow snake
        if snek.head.distance(nomnom) < 15:
            nomnom.refresh()
            snek.grow()
            scoreboard.increase_score()

        # detect collision with wall and end game
        if snek.head.xcor() > 290 or snek.head.xcor() < -290 or snek.head.ycor() > 290 or snek.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()
            scoreboard.watch_walls()

        # detect collision with tail and end game
        for segment in snek.snake_body[1:]:
            if snek.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                scoreboard.watch_yourself()

    # turtle module - 'Screen' method to exit the screen with a mouse click
    screen.exitonclick()


if __name__ == "__main__":
    main()
