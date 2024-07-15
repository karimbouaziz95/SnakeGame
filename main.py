from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from configuration import config


screen = Screen()
screen.setup(width=config["WIDTH"], height=config["HEIGHT"])
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()


screen.listen()
screen.onkeypress(key="Up", fun=snake.snake_up)
screen.onkeypress(key="Down", fun=snake.snake_down)
screen.onkeypress(key="Right", fun=snake.snake_right)
screen.onkeypress(key="Left", fun=snake.snake_left)

scoreboard = ScoreBoard()

while snake.is_alive:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 10:
        food.refresh(snake.get_body_parts_coordinates())
        snake.extend()
        scoreboard.update_score()

    if (
        snake.head.xcor() > config["WIDTH"]/2 - config["MOVE_DISTANCE"] or
        snake.head.xcor() < -(config["WIDTH"]/2 - config["MOVE_DISTANCE"]) or
        snake.head.ycor() > config["HEIGHT"]/2 - config["MOVE_DISTANCE"] or
        snake.head.ycor() < -(config["HEIGHT"]/2 - config["MOVE_DISTANCE"]) 
    ):
        snake.is_alive = False

    for part in snake.body_parts[1:]:
        if snake.head.distance(part) < 10:
            snake.is_alive = False

scoreboard.game_over()
screen.update()
screen.exitonclick()