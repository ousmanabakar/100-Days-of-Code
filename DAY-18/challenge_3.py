from turtle import *
import random

tim = Turtle()
colors = ["dark green", "crimson", "gold", "chartreuse", "magenta", "green", "navy", "yellow", "black"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.fd(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()
