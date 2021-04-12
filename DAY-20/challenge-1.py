from turtle import Turtle, Screen

screen = Screen()

po = [-20, -40, -60]
for i in range(3):
    snake = Turtle("square")
    snake.penup()
    snake.color("white")
    snake.goto(x=po[i], y=0)


screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.exitonclick()


