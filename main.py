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
# car_list = []
car_manager = CarManager()


screen.listen()
screen.onkeypress(player.move, "w")
screen.onkeypress(player.back_move, "s")

# cycle = 0
# level_counter = 1

CarManager.speed_property()

game_is_on = True
while game_is_on:
    time.sleep(0.09)
    screen.update()

    # if cycle == 6:

    car_manager.spawn_cars()
    # CarManager()
    # cycle = 0

    for car in car_manager.car_list:
        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False

        car.move_car()

    if player.ycor() >= 280:
        player.move_to_starting_position()
        scoreboard.update_level()
        car_manager.update_speed()

        # level_counter += 1
    # cycle += 1

screen.exitonclick()