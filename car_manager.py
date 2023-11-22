from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.goto(300 -STARTING_MOVE_DISTANCE, random.randint(-250,250))
        self.setheading(180)

        self.spawned_cars = []
        self.spawned_cars.append(self)

    def move_car(self):
        if self.xcor() > -340:
            self.forward(MOVE_INCREMENT)
        if self.xcor() <= -340:
            self.clear()
    
    def spawn_cars(self):
        number_generator = random.randint(0,4)
        for number in range(number_generator):
            self.spawned_cars.append(CarManager())
        