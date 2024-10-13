import turtle
import pandas


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
score = 0
game_is_on = True
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another State's name?").title()
    if answer == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        to_learn = pandas.DataFrame(states_to_learn)
        to_learn.to_csv("states_to_learn.scv")
        break
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        score += 1
        answer_info = data[data.state == answer]
        x = int(answer_info.x)
        y = int(answer_info.y)
        t.teleport(x, y)
        t.write(answer)
