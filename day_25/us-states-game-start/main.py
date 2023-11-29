import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)



data = pandas.read_csv("./50_states.csv")
data_list = data.state.to_list()
answers = []

while len(answers) < 50:
    answer_state = screen.textinput(title=f"{len(answers)}/50 States Correct", prompt="What's another State name?").title()
    
    row = data[data.state == answer_state]
    x_value = row.iloc[0]['x'] # row.x
    y_value = row.iloc[0]['y'] # row.y

    if answer_state == "Exit":
        break
    if answer_state in data_list:
        answers.append(answer_state)
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(x_value, y_value)
        pen.pendown()
        pen.write(answer_state, font=('Arial', 7, 'normal')) # answer_state.item()
        
missed_states = {
    "state": []
}
        
for state in data_list:
    if state not in answers:
        missed_states["state"].append(state)

ms = pandas.DataFrame(missed_states)
ms.to_csv("states_to_learn.csv")

















# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()