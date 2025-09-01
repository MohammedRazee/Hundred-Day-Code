from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which tutrle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles =[]


y_positions = -120
for n in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(n)
    new_turtle.up()
    new_turtle.goto(x=-230, y=y_positions)

    all_turtles.append(new_turtle)
    y_positions += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} trutle is the winner!")
            else:
                print(f"You've lost! The {winning_color} trutle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

