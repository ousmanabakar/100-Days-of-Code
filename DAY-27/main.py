import tkinter

window = tkinter.Tk()


window.title("My First Gui App")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text 1"
my_label.config(text="New text 2")


#BUTTON
def button_clicked():
    print("I got clicked")
    new_text = my_input.get()
    my_label.config(text=new_text)


my_button = tkinter.Button(text="click me", command=button_clicked)
my_button.pack()

#Entry

my_input = tkinter.Entry()
my_input.pack()
print(my_input.get())




window.mainloop()
