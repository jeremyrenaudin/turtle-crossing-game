import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# initialize the screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing turtle")
screen.tracer(0)

# initialize the game
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# define keys that the screen will detect and their related actions to execute
screen.listen()
screen.onkey(fun=player.go_up, key="Up")

# launch the game
game_is_on = True
while game_is_on:
    time.sleep(0.1) # wait 0.1 second between each screen update (each while loop)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on=False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

# exit the game on click
screen. exitonclick()
