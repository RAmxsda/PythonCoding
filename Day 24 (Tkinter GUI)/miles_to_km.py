from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


root = Tk()
root.title("Simple miles to km converter")
root.minsize(width=200, height=200)
root.config(padx=50, pady=50)

miles_input = Entry(root, width=6)
miles_input.grid(row=0, column=0)

miles_label = Label(root, text="Miles")
miles_label.grid(row=0, column=1)


is_equal_label = Label(root, text="is equal to")
is_equal_label.grid(row=1, column=0)

km_result_label = Label(root, text="0")
km_result_label.grid(row=1, column=1)
km_result_label.config(padx=10)

km_label = Label(root, text="Km")
km_label.grid(row=1, column=2)


calculate_button = Button(root, text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

root.mainloop()

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
