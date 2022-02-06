from tkinter import *

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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    canvas.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_box.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 7:
        timer_time = LONG_BREAK_MIN * 60
        timer_label.config(text="Break", fg=RED)
        count_down(timer_time)

    elif reps % 2 == 0:
        timer_time = SHORT_BREAK_MIN * 60
        timer_label.config(text="Break", fg=PINK)
        count_down(timer_time)

    else:
        timer_time = WORK_MIN * 60
        timer_label.config(text="Work")
        count_down(timer_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        mark = ""
        work_session = reps // 2
        for _ in range(work_session):
            mark += "✓"

        tick_box.config(text=mark)

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

# Timer title
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)

# Reset Button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=3)

# Tick Box
tick_box = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "normal"))
tick_box.grid(column=1, row=4)

window.mainloop()
