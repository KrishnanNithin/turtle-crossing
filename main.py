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

#listener for controls
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    
    car_manager.create_cars()
    car_manager.move_cars(scoreboard.level)
    
    #player wins
    if player.ycor() > 280:
        player.spawn()
        scoreboard.level += 1
        scoreboard.refresh()

    #player dies
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()