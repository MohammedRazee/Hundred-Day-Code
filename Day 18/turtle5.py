import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for n in range(0, 360, size_of_gap):
        tim.color(random_color())
        tim.setheading(n)
        tim.circle(100)

draw_spirograph(2)
screen.exitonclick()
