from tkinter import *
from tkinter import PhotoImage
from timeit import default_timer as timer


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_button.config(state="active")
    root.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    Canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    # if it is 8, 16 or multiple of 8 reps
    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    # if it is 2, 4, 6, ... except multiple of 8 reps
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
        start_button.config(state="disabled")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    Canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        # start_button.config(state="active")
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
            check_mark.config(text=marks, font=(FONT_NAME, 20))


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)
Canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file="/Python 100 days challenge/Day 25(Tkinter game)/tomato.png"
)
Canvas.create_image(100, 112, image=tomato_img)
Canvas.grid(row=1, column=1)
timer_text = Canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)
check_mark.config(pady=20, padx=20)
root.mainloop()
