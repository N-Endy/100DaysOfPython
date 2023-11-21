import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

# Initialize player
player = Player()
screen.onkey(player.move, "Up")

# Initialize car
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
