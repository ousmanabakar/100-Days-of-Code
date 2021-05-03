import tkinter


def miles_to_km():
    miles = float(my_miles_input.get())
    km = round(miles * 1.609, 2)
    my_result_label.config(text=km)



window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=600, height=300)
window.config(padx=20, pady=20)


# Entry
my_miles_input = tkinter.Entry(width=7)
print(my_miles_input.get())
my_miles_input.grid(column=1, row=0)

#labels
my_miles_label = tkinter.Label(font=("Arial", 15, "bold"))
my_miles_label.config(text="Miles")
my_miles_label.grid(column=2, row=0)

my_is_eq_to_label = tkinter.Label(font=("Arial", 15, "bold"))
my_is_eq_to_label.config(text="is equal to")
my_is_eq_to_label.grid(column=0, row=1)

my_result_label = tkinter.Label(font=("Arial", 15, "bold"))
my_result_label.config(text="0")
my_result_label.grid(column=1, row=1)


my_km_label = tkinter.Label(font=("Arial", 15, "bold"))
my_km_label.config(text="Km")
my_km_label.grid(column=2, row=1)

#Button
my_button = tkinter.Button(text="calculate", command=miles_to_km)
my_button.grid(column=1, row=2)






window.mainloop()

