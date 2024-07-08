import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_up, "w")

car_manager.generate_new_car()
i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    i += 1
    if i % 6 == 0:
        car_manager.generate_new_car()

    if car_manager.check_if_made_contact(player):
        scoreboard.game_over()
        game_is_on = False

    if player.reached_finish():
        car_manager.car_speed += 5
        scoreboard.increase_level()
        player.reset_position()

screen.exitonclick()
