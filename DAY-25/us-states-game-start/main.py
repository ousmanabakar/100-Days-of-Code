import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


stats_names = pandas.read_csv("50_states.csv")

FONT = ('monaco', 8, 'bold')

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in stats_names.state:
            if state not in guessed_states:
                missing_states.append(state)

        new_missing_states = pandas.DataFrame(missing_states)
        new_missing_states.to_csv("missing_states.csv")
        break

    for i in stats_names.state:
        if answer_state == i:
            guessed_states.append(answer_state)
            t = Turtle()
            t.hideturtle()
            t.penup()
            new_state = stats_names[stats_names.state == answer_state]
            t.goto(int(new_state.x), int(new_state.y))
            t.write(answer_state, font=FONT, align="center")
