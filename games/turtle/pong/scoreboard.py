from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.refresh()

    def update_r_score(self):
        self.r_score += 1
        self.refresh()

    def update_l_score(self):
        self.l_score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 24, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 24, "normal"))

    def declare_winner(self):
        self.goto(0, 0)
        if self.r_score == self.l_score:
            self.write("GAME OVER. TIE!", align="center", font=("Courier", 24, "normal"))
        elif self.r_score > self.l_score:
            self.write("GAME OVER.\nRIGHT WINS !", align="center", font=("Courier", 24, "normal"))
        else:
            self.write("GAME OVER.\nLEFT WINS !", align="center", font=("Courier", 24, "normal"))