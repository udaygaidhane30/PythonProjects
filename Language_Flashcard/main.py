from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
data_dict = {}

try:
    data_csv = pandas.read_csv("data\words_not_known.csv")

except:
    data_csv = pandas.read_csv("data\lang_french_words.csv")
    data_dict = data_csv.to_dict(orient="records")

else:
    data_dict = data_csv.to_dict(orient="records")


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data_dict)
    canvas.itemconfig(word_text, text=random_word['French'], fill="black")
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(card_image, image=flashcard_1)
    flip_timer = window.after(3000, flip_card)


def is_known():
    data_dict.remove(random_word)
    data = pandas.DataFrame(data_dict)
    print(data)
    data.to_csv("data\words_not_known.csv", index=False)
    next_card()


def flip_card():
    global random_word
    canvas.itemconfig(card_image, image=flashcard_2)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_word["English"], fill="white")


# Ui
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_1 = PhotoImage(file="images\card_front.png")
flashcard_2 = PhotoImage(file="images\card_back.png")
card_image = canvas.create_image(400, 263, image=flashcard_1)
canvas.grid(column=0, row=0, columnspan=2)

# Canvas text
language_text = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
canvas.grid(column=0, row=0)

word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0)

# Right Button
right_image = PhotoImage(file="images\sign_right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

# wrong button
wrong_image = PhotoImage(file="images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

flip_timer = window.after(3000, flip_card)
next_card()

# flip card


window.mainloop()
