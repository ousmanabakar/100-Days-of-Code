from turtle import Turtle, Screen

uzi = Turtle()
screen = Screen()


def move_fd():
    uzi.fd(10)


def move_back():
    uzi.backward(10)


def counter_clockwise():
    new_heading = uzi.heading() + 10
    uzi.setheading(new_heading)



def clockwise():
    new_heading = uzi.heading() - 10
    uzi.setheading(new_heading)


def clear_drawing():
    uzi.reset()


screen.listen()
screen.onkey(fun=move_fd, key="w")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clear_drawing, key="c",)

screen.exitonclick()
