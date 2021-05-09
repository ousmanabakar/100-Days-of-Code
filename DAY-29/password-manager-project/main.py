from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(3, 5))]

    password_numbers = [choice(numbers) for _ in range(randint(3, 5))]

    new_password = password_numbers + password_symbols + password_letters

    shuffle(new_password)
    my_password = "".join(new_password)
    password_entry.insert(0, my_password)
    pyperclip.copy(my_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Warning", message="You should fill all the fields")

    else:
        is_ok = messagebox.askyesno(title=website,
                                    message=f"These are the details entered:\n Email: {email}\n Password: {password}")
        if is_ok:
            with open("data.txt", "a+") as file:
                file.writelines(website + " | " + email + " | " + password + "\n")
                delete_fields()


def delete_fields():
    website_name_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

my_canvas = Canvas(height=200, width=200)
my_logo_img = PhotoImage(file="logo.png")
my_canvas.create_image(100, 100, image=my_logo_img)
my_canvas.grid(column=1, row=0)

# labels
website_name_label = Label(text="Website:")
website_name_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_name_entry = Entry(width=35)
website_name_entry.grid(column=1, row=1, columnspan=2)
website_name_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ousman@email.com")

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

# buttons
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=30, command=save_data)
add_btn.grid(column=1, row=4, columnspan=3)

window.mainloop()
