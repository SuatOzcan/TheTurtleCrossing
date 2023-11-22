import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkeypress(player.move, "w")

cycle = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if cycle == 6:
        car_manager.spawn_cars()
        cycle = 0

    for car in car_manager.spawned_cars:
        car.move_car()

    if player.ycor() >= 280:
        player.move_to_starting_position()
        scoreboard.update_level()

    cycle += 1