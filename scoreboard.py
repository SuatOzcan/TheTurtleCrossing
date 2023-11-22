from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(-280,250)
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-280,250)
        self.level += 1
        self.write(f"Level: {self.level}", font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align = "center", font = FONT)
