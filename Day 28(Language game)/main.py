from tkinter import *
from tkinter import PhotoImage
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("/Python 100 days challenge/Day 28/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(
        "/Python 100 days challenge/Day 28/data/french_words.csv"
    )
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card_img)
    flip_timer = root.after(3000, func=flip_card)


def flip_card():
    print(current_card)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_background, image=back_card_img)
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    # canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv(
        "/Python 100 days challenge/Day 28/data/words_to_learn.csv", index=False
    )

    next_card()


root = Tk()
root.title("FLASH CARD ")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = root.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_card_img = PhotoImage(
    file="/Python 100 days challenge/Day 28/images/card_front.png"
)
back_card_img = PhotoImage(
    file="/Python 100 days challenge/Day 28/images/card_back.png"
)
card_background = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 168, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

right_image = PhotoImage(file="/Python 100 days challenge/Day 28/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)


wrong_image = PhotoImage(file="/Python 100 days challenge/Day 28/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()

root.mainloop()
