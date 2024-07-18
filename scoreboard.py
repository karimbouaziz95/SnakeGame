from turtle import Turtle
from configuration import config

HIGH_SCORE_FILE = "highscore.txt"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open(HIGH_SCORE_FILE) as score_file:            
                self.high_score = int(score_file.read())
        except Exception:
            self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, config["HEIGHT"] / 2 - config["MOVE_DISTANCE"])
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", move=False, align="center", font=('Arial', 20, 'normal'))


    def update_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.display_score()


    def reset_score(self):
        self.score = 0
        self.color("white")
        self.goto(0, config["HEIGHT"] / 2 - config["MOVE_DISTANCE"])
        self.display_score()


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("blue")
        self.write(f"Game over. Restart loading...", move=False, align="center", font=('Arial', 20, 'normal'))
        self.goto(0, -20)
        self.write(f"Final score: {self.score}", move=False, align="center", font=('Arial', 20, 'normal'))
        with open(HIGH_SCORE_FILE, mode="w") as score_file:
            score_file.write(str(self.high_score))
