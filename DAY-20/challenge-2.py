import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

positions = [-20, -40, -60]
snakes_list = []

for i in range(3):
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(x=positions[i], y=0)
    snakes_list.append(snake)


while True:
    screen.update()
    time.sleep(0.1)
    for snake_num in range(len(snakes_list)-1, 0, -1):
        new_x_cor = snakes_list[snake_num - 1].xcor()
        new_y_cor = snakes_list[snake_num - 1].ycor()
        snakes_list[snake_num].goto(new_x_cor, new_y_cor)
    snakes_list[0].forward(20)



screen.exitonclick()


