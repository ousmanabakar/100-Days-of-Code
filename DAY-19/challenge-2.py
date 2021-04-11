from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
colors = ["red", "yellow", "blue", "green", "purple", "black"]
positions = [-70, -40, -10, 20, 50, 80]
list_of_turtles = []

for i in range(0, 6):
    uzi = Turtle("turtle")
    uzi.penup()
    uzi.color(colors[i])
    uzi.goto(x=-230, y=positions[i])
    list_of_turtles.append(i)

if user_bet:
    is_race_on = True
    while is_race_on:
        for turtle in list_of_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You have won. The {winning_color} turtle is the winner!")
                else:
                    print(f"You have lost. The {winning_color} turtle is the winner!")

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            

screen.exitonclick()
