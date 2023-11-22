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
level_counter = 1
car_list = []
# car_manager = CarManager()


screen.listen()
screen.onkeypress(player.move, "w")
screen.onkeypress(player.back_move, "s")

cycle = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if cycle == 6:
        # car_manager.spawn_cars()
        CarManager(car_list)
        cycle = 0

    for car in car_list:  #for car in car_manager.spawned_cars:
        car.move_car(level_counter)

        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        player.move_to_starting_position()
        scoreboard.update_level()
        level_counter += 1

    cycle += 1

screen.exitonclick()