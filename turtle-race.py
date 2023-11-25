import turtle
from turtle import Turtle, Screen
import random


race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle color will win the race?: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_post = [-70, -40, -10, 20, 50, 80]
all_turtles = []
print(f"User choice: {user_bet}")

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-235, y=y_post[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've Won!")
            else:
                print(f"You lost!, {winning_color} is the winner of the race")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
