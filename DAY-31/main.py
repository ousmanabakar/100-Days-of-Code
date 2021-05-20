import random
import time
from tkinter import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_word():
    current_card = random.choice(to_learn)
    my_canvas.itemconfig(card_title, text="French")
    my_canvas.itemconfig(card_word, text=current_card["French"])
    time.sleep(5000)
    card_back_img = PhotoImage(file="images/card_back.png")
    my_canvas.itemconfig(card_front_img, image=card_back_img)
    my_canvas.itemconfig(card_title, text="English")
    my_canvas.itemconfig(card_word, text=current_card["English"])



# def change_card():
#     current_card = random.choice(to_learn)
#     card_back_img = PhotoImage(file="images/card_back.png")
#     my_canvas.itemconfig(card_front_img, image=card_back_img)
#     my_canvas.itemconfig(card_title, text="English")
#     my_canvas.itemconfig(card_word, text=current_card["English"])




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

my_canvas = Canvas(height=526, width=800)

card_front_img = PhotoImage(file="images/card_front.png")
my_canvas.create_image(400, 263, image=card_front_img)
my_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = my_canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = my_canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
my_canvas.grid(row=0, column=0, columnspan=2)

# card_back_img = PhotoImage(file="images/card_back.png")
# my_canvas.create_image(100, 100, image=card_back_img)
# my_canvas.grid(row=0, column=0)

#Buttons
my_wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=my_wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

my_right_image = PhotoImage(file="images/right.png")
right_button = Button(image=my_right_image, highlightthickness=0, command=next_word)
right_button.grid(row=1, column=1)

next_word()
window.mainloop()
