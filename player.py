from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed("fastest")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)    

    def move(self):
        self.forward(20)
    
    def back_move(self):
        self.forward(-20)

    def move_to_starting_position(self):
        self.goto(STARTING_POSITION)
