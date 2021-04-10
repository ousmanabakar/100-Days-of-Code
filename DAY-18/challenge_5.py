import turtle as t
import random

uzi = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = r, g, b

    return rgb_color


uzi.speed(100)


def draw_spirograph(grap_size):
    for _ in range(int(360 / grap_size)):
        uzi.color(random_color())
        uzi.circle(100)
        first_heading = uzi.heading()
        uzi.setheading(first_heading + grap_size)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
