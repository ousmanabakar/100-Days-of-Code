from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 3-control the snake with keypress
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head_of_the_snake.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head_of_the_snake.xcor() > 280 or snake.head_of_the_snake.xcor() < -280 or snake.head_of_the_snake.ycor() > 280 or snake.head_of_the_snake.ycor() < -280:
        scoreboard.reset_game()
        snake.reset_game()
    #   # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head_of_the_snake:
            pass
        elif snake.head_of_the_snake.distance(segment) < 10:
            scoreboard.reset_game()
            snake.reset_game()


screen.exitonclick()
