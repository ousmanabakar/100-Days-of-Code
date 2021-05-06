from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import messagebox
from tkinter.messagebox import showinfo

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    my_start_btn.config(state="normal")
    my_reset_btn.config(state="disabled")

    window.after_cancel(timer)
    my_canvas.itemconfig(timer_text, text="00:00")
    my_title_label.config(text="Timer")
    my_check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    my_start_btn.config(state="disabled")
    my_reset_btn.config(state="normal")
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        #messagebox.showinfo(title="Break", message="Long break!")
        my_title_label.config(text="Break", fg=RED, font=(FONT_NAME, 50))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        #messagebox.showinfo(title="Work", message="Small break!")
        my_title_label.config(text="Break", fg=PINK, font=(FONT_NAME, 50))
        count_down(short_break_sec)
    else:
        #messagebox.showinfo(title="Work", message="Start working~")
        count_down(work_sec)
        my_title_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 50))




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0"+str(count_sec)

    my_canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "v"
        my_check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Label
my_title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))

my_title_label.grid(column=1, row=0)

my_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
my_canvas.create_image(100, 112, image=tomato_image)
timer_text = my_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
my_canvas.grid(column=1, row=1)



# Buttons
my_start_btn = Button(text="Start", highlightthickness=0, command=start_timer, state="normal")
my_start_btn.grid(column=0, row=2)

my_reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer, state="disabled")
my_reset_btn.grid(column=2, row=2)

my_check_mark = Label(fg=GREEN, highlightthickness=0)
my_check_mark.grid(column=1, row=3)

window.mainloop()
