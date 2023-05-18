from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
position = 0
screen.bgcolor('black')
screen.title('Snake game')
pos = [(0, 0), (-20, 0), (-40, 0)]
snake = []
for num in pos:
    tail = Turtle('square')
    tail.color('white')
    tail.penup()
    tail.goto(num)
    snake.append(tail)
    # position -= 20
screen.update()
game_on = True
while game_on:
    # screen.update()
    time.sleep(0.1 )
    for i in range(len(snake)-1, 0, -1):
        snake[i].goto(snake[i-1].xcor(), snake[i-1].ycor())
    snake[0].forward(20)
    snake[0].left(90)
screen.exitonclick()
