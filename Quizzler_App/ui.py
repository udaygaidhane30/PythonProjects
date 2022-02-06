from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Text goes here", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2)

        # Score Label
        self.score_label = Label(text="Score = 0", font=("Arial", 12, "bold"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Right Button
        right_image = PhotoImage(file="images/true.png")
        self.r_button = Button(image=right_image, highlightthickness=0, command=self.true_pressed)
        self.r_button.grid(column=1, row=2, pady=10)

        # Wrong Button
        wrong_image = PhotoImage(file="images/false.png")
        self.w_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        self.w_button.grid(column=0, row=2, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score = {self.quiz.score}")
            q_text = self.quiz.next_question()

            self.canvas.itemconfig(self.question_text, text=f"{q_text}")

        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the END with a score of {self.quiz.score}")
            self.r_button.config(state="disabled")
            self.w_button.config(state="disabled")

    def true_pressed(self):
        response = self.quiz.check_answer("True")
        self.respond(response)

    def false_pressed(self):
        response = self.quiz.check_answer("False")
        self.respond(response)

    def respond(self, response):
        if response:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
