import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
turtles = turtle.Turtle()
data = pandas.read_csv("50_states.csv")
missed_state = []
guess_state = []
all_state = []

for i in range(len(data.state)):
    all_state.append(data.state[i])
while len(guess_state) < 50:
    guess = screen.textinput(title=f'{len(guess_state)}/50 States correct', prompt='Your guess: ').capitalize()
    if guess == 'Exit':
        break
    if guess in all_state:
        guess_state.append(guess)
        check = data[data.state == guess]
        turtles.hideturtle()
        turtles.penup()
        turtles.goto(int(check.x.iloc[0]), int(check.y.iloc[0]))
        turtles.write(guess)
for state in all_state:
    if state not in guess_state:
        missed_state.append(state)
miss_data = pandas.DataFrame(missed_state)
miss_data.to_csv('Missed guess states.csv')



# screen.exitonclick()
