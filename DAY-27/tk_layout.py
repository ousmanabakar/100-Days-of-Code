import tkinter


def button_clicked():
    print("I got clicked")
    new_text = my_input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()

window.title("My First Gui App")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New text 2")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Button
my_button = tkinter.Button(text="click me", command=button_clicked)
# my_button.place(x=50, y=50)
my_button.grid(column=1, row=1)
# my_button.config(padx=20, pady=20)

new_button = tkinter.Button(text="new button")
# my_button.place(x=50, y=50)
new_button.grid(column=2, row=0)

# Entry

my_input = tkinter.Entry()
print(my_input.get())
# my_input.place(x=100, y=100)
my_input.grid(column=2, row=2)


window.mainloop()