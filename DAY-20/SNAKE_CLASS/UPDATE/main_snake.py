from turtle import Screen
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# 3-control the snake with keypress
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



while True:
    screen.update()
    time.sleep(0.1)

    snake.move()




screen.exitonclick()
