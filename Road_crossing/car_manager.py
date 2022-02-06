from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.m_distance = STARTING_MOVE_DISTANCE
        self.traffic = []

    def generate_car(self):
        i = random.randint(1, 10)
        if i == 2:
            car = Turtle("square")
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            y_coor = random.randint(-250, 250)
            car.goto(300, y_coor)
            self.traffic.append(car)

    def move_cars(self):
        for car in self.traffic:
            car.backward(self.m_distance)

    def collision(self, coordinates):
        for car in self.traffic:
            if car.distance(coordinates) < 20:
                return 1

    def level_up(self):
        self.m_distance += MOVE_INCREMENT
