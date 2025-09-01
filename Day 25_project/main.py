import pandas as pd
import turtle


state_location = pd.read_csv("50_states.csv")
check_state = []
for state in state_location.state:
    check_state.append(state.lower())


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_States_img.gif"
screen.addshape(image)
turtle.shape(image)

def got_state(state_name):
    row = state_location[state_location["state"] == state_name]
    x = row["x"].iloc[0]
    y = row["y"].iloc[0]
    turtle.teleport(x, y)
    turtle.write(state_name)
    turtle.teleport(0, 0)


game_is_on = True
done_state = []

while len(done_state) < 50:
    answer_state = screen.textinput(title=f"{len(done_state)}/ 50 states", prompt="What's another state's name?")
    answer_state = answer_state.lower()

    if answer_state == "exit":
        #missed_state = list(set(check_state) - set(done_state))
        missed_state = [n for n in check_state if n not in done_state]
        missed_state_dict = pd.DataFrame(missed_state)
        missed_state_dict.to_csv("learning.csv")
        break

    if answer_state in check_state:
        if answer_state not in done_state:
            done_state.append(answer_state)
            got_state(answer_state.title())
            turtle.update()


