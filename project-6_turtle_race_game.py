import turtle
import random

color_list = ["violet", "red", "blue", "green", "yellow", "orange"]
turtle_list = []
winner_turtle = ""
is_race_on = True


screen = turtle.Screen()
screen.setup(500,400)
user_color = screen.textinput(f"Turtle Race", f"Place your bets on the following colored turtles : {color_list}").lower()

# CREATING 6 TURTLES WITH THEIR DIFFERENT COLORS

for i in range(0, 6):
    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.color(color_list[i])
    turtle_list.append(timmy)

# ADJUST EACH TIMMY AT THEIR APPROPRIATE POSITIONS
intitial_position = -150
for obj in turtle_list:
    obj.penup()
    obj.goto(-200, intitial_position)
    intitial_position+=50

# CODE FOR THE COUNTDOWN
timmy = turtle.Turtle()
turtle.delay(500)
timmy.write("3")
timmy.clear()
turtle.delay(500)
timmy.write("2")
timmy.clear()
turtle.delay(500)

timmy.write("1")
timmy.clear()
turtle.delay(500)

timmy.write("GO!")
timmy.clear()
timmy.hideturtle()

# turtle.write("Hello")

turtle.delay(10)
if user_color in color_list:
    while is_race_on:
        for turtles in turtle_list:
            each_distance = random.randint(0,10)
            turtles.forward(each_distance)
            if turtles.xcor() > 230:
                is_race_on = False
                winner_turtle = turtles.fillcolor()

    temp_turtle = turtle.Turtle()
    temp_turtle.back(200)
    temp_turtle.penup()
    if winner_turtle == user_color:
        temp_turtle.pencolor("green")
        temp_turtle.write(f"YOU WON!\n{winner_turtle} Won the RACE!")

    else:
        temp_turtle.pencolor("red")
        temp_turtle.write(f"YOU LOST!\n{winner_turtle} Won the RACE!")


else:
    print("Color is not available!")
    exit()

screen.exitonclick()
