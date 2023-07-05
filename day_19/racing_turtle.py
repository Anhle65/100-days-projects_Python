from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color:")
color = ['yellow', 'green', 'red', 'blue', 'orange', 'white', 'purple']
y_position = -100
turtles = []
for index in range(6):
    tim = Turtle(shape='turtle')
    tim.color(color[index])
    turtles.append(tim)
    tim.penup()
    tim.goto(x=-280, y=y_position)
    y_position += 50
condition = True
while condition:
    for turtle in turtles:
        turtle.forward((random.randint(0, 10)))
        if turtle.xcor() >= 280:
            condition = False
            if user_bet == turtle.pencolor():
                print(f"You win. The {turtle.pencolor()} turtle win")
            else:
                print(f"The winner is the {turtle.pencolor()} one.")

screen.exitonclick()