from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.writescore()

    def writescore(self):
        self.clear()
        self.write(f"Level={self.level}", font=FONT)

    def next_level(self):
        self.level += 1
        self.writescore()

    def game_over(self):
        self.goto(-70,0)
        self.write("GAME OVER",font=FONT)
