from turtle import Turtle, Screen
import pandas as pd

IMAGE = "blank_states_img.gif"
data = pd.read_csv("50_states.csv")

screen = Screen()
screen.addshape(IMAGE)  # register image as a shape to be able to access turtle as shape.
bg_image = Turtle(IMAGE)

# ----- CODE BODY -----
guessed_state = []

while len(guessed_state) < 50:

    user_input = screen.textinput(f"U.S. States Game {len(guessed_state)}/50",
                                  "Please enter a state:").title()

    state_list = data.state.to_list()

    if user_input == "Exit":
        break   # break the loop

    if user_input in state_list:

        guessed_state.append(user_input)

        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        row = data[data.state == user_input]    # get the specific row
        # turtle.goto(x=int(row.x), y=int(row.y))
        turtle.goto(int(row.x.iloc[0]), int(row.y.iloc[0]))   # get column x and y with index 0.
        turtle.write(user_input)


other_states = []
for state in data.state:
    if state not in guessed_state:
        other_states.append(state)

data_dict = {
    "Other states": other_states
}

pd.DataFrame(data_dict).to_csv("states_to_learn.csv")

