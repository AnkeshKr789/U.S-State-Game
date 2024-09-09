import turtle
import pandas


screen = turtle.Screen()
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
screen.title("U.S State Game")
turtle.shape(image)

data = pandas.read_csv("day-25-us-states-game-start/50_states.csv")
all_states = data["state"].to_list()
already_answer = []
game_is_on = 0

while game_is_on != 50:
    answer_state = screen.textinput(
        title=(f"{game_is_on}/50"), prompt="What's another state name ?"
    ).title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in already_answer:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("day-25-us-states-game-start/states_to_learn.csv")
        break

    if answer_state in all_states:
        if answer_state not in already_answer:
            already_answer.append(answer_state)
            game_is_on += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)

    if game_is_on == 50:
        reset = screen.textinput(
            title="Play Again", prompt="Do you want to play agains? Y/N"
        ).lower()
        if reset == "y":
            already_answer = []
            game_is_on = 0
            t.clear()
