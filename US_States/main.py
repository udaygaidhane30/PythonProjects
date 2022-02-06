import pandas
from turtle import Screen, Turtle

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
timmy = Turtle(image)
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
game_is_on = True
qwerty = Turtle()
qwerty.hideturtle()
qwerty.penup()
input_states = []
need_to_learn = []

while len(input_states) < 50:
    inp_state = (screen.textinput(f"{len(input_states)}/50 Guess the States", "What's the another state? ")).title()
    if inp_state == "Exit":
        # for states in all_states:
        #     if states not in input_states:
        #         need_to_learn.append(states)
        need_to_learn = [state for state in all_states if state not in input_states]
        csv_file = pandas.DataFrame(need_to_learn)
        csv_file.to_csv("Need_to_learn_states.csv")
        break

    if inp_state in all_states:
        input_states.append(inp_state)
        state_data = data[data.state == inp_state]
        xcor = int(state_data["x"])
        ycor = int(state_data["y"])
        qwerty.goto(xcor, ycor)
        qwerty.write(f"{inp_state}", align="center")
