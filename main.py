"""Main Function"""
import turtle
import random

# Trigger for race to start
race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple",]
y_positions = [-70, -40, -10, 20, 50, 80,]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.speed("fastest")
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    # Creating a LIST OF OBJECTS
    # Each object has its own state
    all_turtles.append(new_turtle)

if user_bet:
    # Trigger race to start
    race_on = True

while race_on:
    # Cycling through each turtle object
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
