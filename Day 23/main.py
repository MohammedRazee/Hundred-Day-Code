import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(tim.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for any_car in car.all_cars:
        if tim.distance(any_car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if tim.ycor() > 280:
        tim.reset_position()
        car.level_up()
        scoreboard.level_up()


screen.exitonclick()
