import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def walk_tim():
    angles = [0, 90, 180, 270]
    tim.pensize(5)
    tim.hideturtle()
    tim.speed("fastest")

    for _ in range(200):
        tim.color((random_color()))
        tim.fd(20)
        tim.setheading(random.choice(angles))

walk_tim()
screen = t.Screen()
screen.exitonclick()
