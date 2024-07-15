from turtle import Turtle
import random
from configuration import config


class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh(config["STARTING_POSITIONS"])


    def refresh(self, occupied_by_snake):
        random_x = random.randrange(-(config["WIDTH"] // 2) + config["MOVE_DISTANCE"], (config["WIDTH"] // 2) - config["MOVE_DISTANCE"], 20)
        random_y = random.randrange(-(config["WIDTH"] // 2) + config["MOVE_DISTANCE"], (config["WIDTH"] // 2) - config["MOVE_DISTANCE"], 20)
        while [random_x, random_y] in occupied_by_snake:
            random_x = random.randrange(-(config["WIDTH"] // 2) + config["MOVE_DISTANCE"], (config["WIDTH"] // 2) - config["MOVE_DISTANCE"], 20)
            random_y = random.randrange(-(config["WIDTH"] // 2) + config["MOVE_DISTANCE"], (config["WIDTH"] // 2) - config["MOVE_DISTANCE"], 20)
        self.goto(random_x, random_y)
        