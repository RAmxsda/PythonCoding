from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    pasword_letters = []
    for _ in range(randint(5, 7)):
        pasword_letters.append(choice(letters))
    # pasword_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = pasword_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    Website = website_entry.get()
    Email = email_entry.get()
    Password = password_entry.get()

    new_data = {
        Website: {
            "email": Email,
            "password": Password,
            "username": Email.split("@")[0],
        }
    }
    if len(Website) == 0 or Email == "@email.com" or len(Password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        try:
            with open(
                "/Python 100 days challenge/Day 26 (Password Manager)/data.json", "r"
            ) as json_data:
                # Reading json data
                data = json.load(json_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
        # Updating data
        data.update(new_data)
        # Writing updated data
        with open(
            "/Python 100 days challenge/Day 26 (Password Manager)/data.json", "w"
        ) as json_data:
            json.dump(data, json_data, indent=4)

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ----------------------------- Search --------------------------------#


def search():
    website = website_entry.get()
    try:
        with open(
            "/Python 100 days challenge/Day 26 (Password Manager)/data.json", "r"
        ) as json_data:
            data = json.load(json_data)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Error", message="No Data File Found. Please add a password."
        )
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website,
                message=f"Email: {email}\nPassword: {password}",
            )
        else:
            messagebox.showinfo(
                title="Error",
                message=f"No details for {website} exists. Please add a password.",
            )


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(
    file="/Python 100 days challenge/Day 26 (Password Manager)/logo.png"
)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "@email.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)


# Buttons
search_button = Button(text="Search", width=14, bg="yellow", command=search)
search_button.grid(row=1, column=3)
generate_password_button = Button(
    text="Generate Password", width=14, bg="pink", command=create_password
)
generate_password_button.grid(row=3, column=3)


add_button = Button(text="Add", width=16, bg="green", command=save)
add_button.grid(row=4, column=1, columnspan=2)
add_button.config(pady=5)


root.mainloop()
