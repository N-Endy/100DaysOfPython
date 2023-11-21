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

# Initialize Scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    # Detect Player win
    if player.ycor() == 300:
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.level_up()
