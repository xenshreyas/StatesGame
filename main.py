import tkinter
import pandas
import turtle
from turtle import Turtle

window = tkinter.Tk()
window.title("State/Province Game")
window.minsize(width=100, height=100)

button1 = tkinter.Button(text="U.S. Map")
button1.grid(column=0, row=0)

button2 = tkinter.Button(text="Canada Map")
button2.grid(column=1, row=0)


def run_us():
    screen = turtle.Screen()
    screen.title("The States Game")
    image = "data/blank_states_img.gif"
    screen.addshape(image)

    turtle.shape(image)

    data = pandas.read_csv("data/us_states.csv")

    states = data.state.to_list()
    x_coordinates = data.x.to_list()
    y_coordinates = data.y.to_list()

    guessed_states = []

    while len(guessed_states) < 50:
        if len(guessed_states) == 0:
            answer_state = screen.textinput(title="Guess the State",
                                            prompt="What's another state's name?").title()
        else:
            answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                            prompt="What's another state's name?")

        if answer_state == "Exit":
            missing_states = []
            for state in states:
                if state not in guessed_states:
                    missing_states.append(state)

            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("data/states_to_learn.csv")
            screen.bye()
            break

        check_state(answer_state, guessed_states, states, x_coordinates, y_coordinates)

    screen.listen()

    turtle.mainloop()


# If button 2 is clicked, new window opens with Canada map
def run_canada():
    screen = turtle.Screen()
    screen.title("The Provinces Game")
    image = "data/blank_provinces_img.gif"
    screen.addshape(image)

    turtle.shape(image)

    data = pandas.read_csv("data/canada_provinces.csv")

    provinces = data.province.to_list()
    x_coordinates = data.x.to_list()
    y_coordinates = data.y.to_list()

    guessed_provinces = []

    while len(guessed_provinces) < 13:
        if len(guessed_provinces) == 0:
            answer_province = screen.textinput(title="Guess the Province",
                                               prompt="What's another province's name?").title()
        else:
            answer_province = screen.textinput(title=f"{len(guessed_provinces)}/13 Provinces Correct",
                                               prompt="What's another province's name?")

        if answer_province == "Exit":
            missing_provinces = []
            for province in provinces:
                if province not in guessed_provinces:
                    missing_provinces.append(province)

            new_data = pandas.DataFrame(missing_provinces)
            new_data.to_csv("data/provinces_to_learn.csv")
            screen.bye()
            break

        check_state(answer_province, guessed_provinces, provinces, x_coordinates, y_coordinates)

    screen.listen()

    turtle.mainloop()


def check_state(answer_province, guessed_provinces, provinces, x_coordinates, y_coordinates):
    if answer_province in provinces:
        guessed_provinces.append(answer_province)
        t = Turtle()
        t.hideturtle()
        t.penup()
        province_index = provinces.index(answer_province)
        t.goto(x_coordinates[province_index], y_coordinates[province_index])
        t.write(answer_province)


button1.config(command=run_us)
button2.config(command=run_canada)

window.mainloop()
