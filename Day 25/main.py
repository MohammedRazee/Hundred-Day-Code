import turtle
import pandas as pd
import time

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
correct_guesses = []
run_game = True

def game_over():
    over = turtle.Turtle()
    over.penup()
    over.hideturtle()
    over.goto((-150,0))
    over.write("Better Luck Next Time", font=("Arial", 20, "bold"))


def correct_guess(answer):
    temp = states_data[states_data["state"].str.lower() == answer.lower()]
    return not temp.empty
        
def update_map(answer):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()

    data = states_data[states_data["state"].str.lower() == answer.lower()]
    x = data.x.item()
    y = data.y.item()

    writer.goto(x,y)
    writer.write(data["state"].item())

def victory():
    tim = turtle.Turtle()
    tim.penup()
    tim.hideturtle()
    tim.goto((-100,0))
    tim.write("Congratulations", font=("Arial", 20, "bold"))



while run_game:
    answer_state = turtle.textinput(title=f"{len(correct_guesses)} / 50 Guessed Correct", prompt="What's another state's name?")
    if answer_state.lower() == "done":
        game_over()
        time.sleep(1)
        run_game = False

    if correct_guess(answer_state):
        if answer_state not in correct_guesses:
            correct_guesses.append(answer_state)
            update_map(answer_state)
        turtle.update()

    if len(correct_guesses) == 50:
        victory()
        run_game = False

all_states = states_data["state"].to_list()
missed_states = [item for item in all_states if item.lower() not in correct_guesses]

last = pd.DataFrame(missed_states, columns=["Missed States"])
last.to_csv("get_good.csv")
