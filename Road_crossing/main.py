import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(fun=player.move, key="Up")
car = CarManager()
points = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_cars()
    if player.ycor() == 280:
        points.next_level()
        player.new_level()
        car.level_up()
    if car.collision((player.xcor(), player.ycor())) == 1:
        points.game_over()
        game_is_on = False

screen.exitonclick()
