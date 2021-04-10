# from turtle import *
import turtle as t
import random

# colors = ["dark green", "crimson", "gold", "chartreuse", "magenta", "green", "navy", "yellow", "black"]

uzi = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = r, g, b

    return rgb_color


directions = [0, 90, 180, 270]

for _ in range(200):
    uzi.speed(100)
    uzi.pensize(10)
    uzi.pencolor(random_color())

    uzi.right(random.choice(directions))

    uzi.fd(30)
    uzi.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
