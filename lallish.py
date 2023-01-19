from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic('road.gif')

bet_money = int(input("Choose an amount you wish to bet: "))
bet_turtle = (input("Choose which horse to bet on: "))

y_positions = [-260, -172, -85, 2, 85, 172, 260]
color = ["white", "red", "orange", "pink", "tomato", "dodgerblue", "yellow"]
all_turtle = []
for index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2)
    new_turtle.speed('fastest')
    new_turtle.penup()
    new_turtle.goto(x=-350, y=y_positions[index])
    new_turtle.color(color[index])
    all_turtle.append(new_turtle)


on = True

while on:
    for turtle in all_turtle:
        if turtle.xcor() > 330:
            on = False
            winner = turtle.pencolor()
            if winner == bet_turtle:
                print(f'You win! {winner} came 1st place!')
            else:
                print(f'You loose! {winner} came 1st place!')
        random_speed = random.randint(0, 18)
        turtle.forward(random_speed)


screen.exitonclick()
