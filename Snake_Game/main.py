from snake import Snake
from turtle import Screen
from food import Food
import time
from score import Score

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.xcor() > 350 or snake.head.xcor() < -350 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        score.game_over()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.point()
        snake.extend()
    snake.move()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
