from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

point = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncewall()

    if ball.xcor() > 330 and ball.distance(r_paddle) < 50:
        ball.bouncepaddle()

    if ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bouncepaddle()

    if ball.xcor() > 380:
        ball.restart()
        point.l_point()

    if ball.xcor() < -380:
        ball.restart()
        point.r_point()

screen.exitonclick()
