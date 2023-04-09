import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("lightsteelblue1")
screen.title("Turtle Pedestrian")
screen.tracer(0)

# Creating a player turtle
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:

    # Screen updates every 0.1 seconds
    time.sleep(0.1)
    screen.update()

    # Slow down the creation of the cars
    random_chance = random.randint(1, 6)
    if random_chance == 1:
        car_manager.create_car()

    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect turtle has crossed the road
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
