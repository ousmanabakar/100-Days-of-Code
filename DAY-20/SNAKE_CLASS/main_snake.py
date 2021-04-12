from turtle import Screen
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

while True:
    screen.update()
    time.sleep(0.1)

    snake.move()




screen.exitonclick()
