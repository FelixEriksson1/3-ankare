import random
from turtle import Turtle, Screen


class spelare_info():
    def __init__(self, money, level):

        self.money = money
        self.level = level


player = spelare_info(400, 1)


bet = int(input("Enter your bet: "))


race_active = False
screen = Screen()
screen.setup(width=500, height=400)
turtle_bet = screen.textinput(
    title="Make your bet!", prompt="Which turtle do you think will win? Enter a colour: ")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = (-100, -60, -20, 20, 60, 100)
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=(y_positions[turtle_index]))
    all_turtles.append(new_turtle)

    if turtle_bet:
        race_active = True

    while race_active:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                race_active = False
                winning_colour = turtle.pencolor()
                if winning_colour == turtle_bet:
                    vinst = bet*5
                    print(
                        f"You win! The {winning_colour} turtle is the winner. You won {vinst} ")

                else:
                    vinst = vinst-bet
                    print(
                        f"You lose. The {winning_colour} turtle is the winner.")

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

        screen.exitonclick()
