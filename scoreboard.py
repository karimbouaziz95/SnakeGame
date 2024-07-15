from turtle import Turtle
from configuration import config


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, config["HEIGHT"] / 2 - config["MOVE_DISTANCE"])
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 20, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("blue")
        self.write(f"Game over.", move=False, align="center", font=('Arial', 20, 'normal'))
        self.goto(0, -20)
        self.write(f"Final score: {self.score}", move=False, align="center", font=('Arial', 20, 'normal'))
