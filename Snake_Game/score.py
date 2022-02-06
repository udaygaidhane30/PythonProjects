from turtle import Turtle
ALIGNMENT = "center"
FONT = 'tuple["Courier",24,"normal"]'


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 290)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align=ALIGNMENT, font=FONT)