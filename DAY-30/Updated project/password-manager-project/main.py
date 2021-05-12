from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


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

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Warning", message="You should fill all the fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            reset_fields()

# ---------------------------- RESET FIELDS ------------------------------- #


def reset_fields():
    website_name_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    email_entry.insert(0, "example@email.com")


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_name_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="error", message="This data does not exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="error", message=f"No data for this '{website}' website exists")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

my_canvas = Canvas(height=200, width=200)
my_logo_img = PhotoImage(file="logo.png")
my_canvas.create_image(100, 100, image=my_logo_img)
my_canvas.grid(row=0, column=1)

# labels
website_name_label = Label(text="Website:")
website_name_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_name_entry = Entry(width=30)
website_name_entry.grid(row=1, column=1)
website_name_entry.focus()

email_entry = Entry(width=48)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@email.com")

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

# buttons
search_btn = Button(text="Search", width=11, command=find_password)
search_btn.grid(row=1, column=2)

generate_password_btn = Button(text="Generate Password", width=14, command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=41, command=save_data)
add_btn.grid(row=4, column=1, columnspan=3)

window.mainloop()
