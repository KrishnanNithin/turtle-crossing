from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self) -> None:
        self.cars = []

    def create_cars(self):
        chance = randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color((choice(COLORS)))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self, level):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE+(MOVE_INCREMENT*level))
