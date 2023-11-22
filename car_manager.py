from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self, list):
        super().__init__()

        self.hideturtle()  

        for i in range(random.randint(1,5)):
            list.append(Car())
    
    def spawn_cars(self):
        number_generator = random.randint(0,4)
        for number in range(number_generator):
            self.spawned_cars.append(CarManager())


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        # self.speed = MOVE_INCREMENT * level
        self.goto(300 -STARTING_MOVE_DISTANCE, random.randint(-250,250))
        self.setheading(180)
    
    def move_car(self, level):
        if self.xcor() > -340:
            self.forward(MOVE_INCREMENT * level)
        if self.xcor() <= -340:
            self.clear()