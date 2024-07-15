from turtle import Turtle
from configuration import config

class Snake:
    def __init__(self):
        self.body_parts = []
        self.length = 0
        self.head = None
        self.is_alive = True
        self.create_snake()

    def create_snake(self):
        for position in [tuple(item) for item in config["STARTING_POSITIONS"]]:
            mbappe = Turtle(shape="square")
            mbappe.penup()
            mbappe.color("white")
            mbappe.goto(position)
            self.body_parts.append(mbappe)
            self.length += 1
        self.head = self.body_parts[0]

    def get_body_parts_coordinates(self):
        return [[int(round(mbappe.xcor(), 2)), int(round(mbappe.ycor(), 2))] for mbappe in self.body_parts]
    
    def get_head_coordinates(self):
        return (int(round(self.head.xcor(), 2)), int(round(self.head.ycor(), 2)))

    def move(self):
        for i in range(self.length-1, 0, -1):
            new_x = self.body_parts[i-1].xcor()
            new_y = self.body_parts[i-1].ycor()
            self.body_parts[i].goto(new_x, new_y)
            self.body_parts[i].setheading(self.body_parts[i-1].heading())
        self.head.forward(config["MOVE_DISTANCE"])

    def extend(self):
        tail = self.body_parts[-1]
        mbappe = Turtle(shape="square")
        mbappe.penup()
        mbappe.color("white")
        if tail.heading() == 0:
            mbappe.goto(tail.xcor() - 20, tail.ycor())
        elif tail.heading() == 180:
            mbappe.goto(tail.xcor() + 20, tail.ycor())
        elif tail.heading() == 90:
            mbappe.goto(tail.xcor(), tail.ycor() - 20)
        elif tail.heading() == 270:
            mbappe.goto(tail.xcor(), tail.ycor() + 20)
        self.length += 1
        self.body_parts.append(mbappe)


    def snake_up(self):
        if self.head.heading() != config["DOWN"]:
            self.head.setheading(config["UP"])

    def snake_down(self):
        if self.head.heading() != config["UP"]:
            self.head.setheading(config["DOWN"])

    def snake_right(self):
        if self.head.heading() != config["LEFT"]:
            self.head.setheading(config["RIGHT"])

    def snake_left(self):
        if self.head.heading() != config["RIGHT"]:
            self.head.setheading(config["LEFT"])
