from tkinter import *


def action():
    miles = float(entry.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


# this is first GUI trial with tkinter
window = Tk()
window.title("First try")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="is equal to")
my_label.grid(column=0, row=1)

# TextBox
# my_textbox = Text(height=2, width=5)
# my_textbox.focus()
# input_value = (my_textbox.get("1.0", END))
# my_textbox.grid(column=1, row=0)

# miles input

entry = Entry(width=7)
entry.grid(column=1, row=0)

# label2
my_label2 = Label(text="Miles")
my_label2.grid(column=2, row=0)

# label3
my_label3 = Label(text="km")
my_label3.grid(column=2, row=1)

# result_label
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# button
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

window.mainloop()

# def add(*args):
#     """here unlimited arguments can be passed"""
#     result = 0
#     for element in args:
#         result += element
#
#     return result
#
#
# print(add(65, 25, 5, 5))

# my_list = [3, 4, 5, 6]
# print(*my_list, sep="/")
