from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.car_list = []   
    
    def spawn_cars(self):
        random_integer = random.randint(1,6)
        if random_integer == 1:
            number_generator = random.randint(0,4)
            for number in range(number_generator):
                self.car_list.append(Car())

    @classmethod
    def speed_property(cls):
        cls.car_speed = STARTING_MOVE_DISTANCE

    @classmethod
    def send_car_speed(cls):
        return cls.car_speed
    
    @classmethod
    def update_speed(cls):
        cls.car_speed += MOVE_INCREMENT

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
    
    def move_car(self):
        if self.xcor() > -340:
            self.forward(CarManager.send_car_speed())  # self.forward(MOVE_INCREMENT * level)
        if self.xcor() <= -340: # Clear turtle when it is out of the screen.
            self.clear()