import random
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode()
#can use import turle as t
#t will be an alternative word of the name module
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
timmy = Turtle()
timmy.shape('turtle')
timmy.color('Darkgrey')
timmy.speed('fastest')
current = timmy.heading()
print(current)
timmy.right(10)
while timmy.heading() != current:
    # timmy.color(random_color())
    timmy.circle(90)
    timmy.right(20)
j = 3
# for i in range(10):
#     for m in range(j):
#         timmy.step
#         # timmy.right(360/j)
#     j += 1
print(timmy)

my_screen = Screen()
# print(my_screen.canvheight)
my_screen.exitonclick()
# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column('Name',['Mom','Dad','Brother','Me'])
# table.add_column('age',[1974,1971,2000,2002])
#
# print(table)