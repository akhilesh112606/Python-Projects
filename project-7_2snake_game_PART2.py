import random
import time
from turtle import Screen
from turtle import Turtle

import food

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


# IMPORTING OF ALL FUNCTIONS
class Snake:
    turtles_list = []

    # CONSTRUCTOR CREATION
    def __init__(self):
        for i in range(0, 3):
            timmy = Turtle()
            timmy.penup()
            timmy.shape("square")
            timmy.color("white")
            timmy.goto(y=0, x=(-20) * i)
            self.turtles_list.append(timmy)
        self.turtles_list[0].shape("turtle")

    def move(self, score):
        global MOVE_DISTANCE
        distance = MOVE_DISTANCE
        for seg_num in range(len(self.turtles_list) - 1, 0, -1):
            self.turtles_list[seg_num].goto(self.turtles_list[seg_num - 1].position())

        if score%5==0 and score!=0:
            if score >= 5 and score<10:
                distance*=1.2
            elif score>=10 and score<15:
                distance*=1.5
            else:
                distance*=2
        self.turtles_list[0].forward(distance)
        self.turtles_list[-1].showturtle()

    def up(self):
        if self.turtles_list[0].heading() != DOWN:
            self.turtles_list[0].setheading(90)

    def down(self):
        if self.turtles_list[0].heading() != UP:
            self.turtles_list[0].setheading(270)

    def right(self):
        if self.turtles_list[0].heading() != LEFT:
            self.turtles_list[0].setheading(0)

    def left(self):
        if self.turtles_list[0].heading() != RIGHT:
            self.turtles_list[0].setheading(180)

    def position(self):
        return self.turtles_list[0].pos()

    def increase_snake_body(self):
        timmy = Turtle()
        timmy.penup()
        timmy.shape("square")
        timmy.color("white")
        self.turtles_list.append(timmy)
        self.turtles_list[-1].hideturtle()


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.dot_turtle = Turtle()
        self.dot_turtle.shape("circle")
        self.dot_turtle.penup()
        self.dot_turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # In General the size of the shape is 20/20, we have converted it to 10/10 using 0.5
        self.dot_turtle.color("red")
        self.dot_turtle.speed("fastest")
        # self.dot_turtle.goto(x = random.randint(-280, 280), y=random.randint(-280, 280))
        self.new_position_food()

    def new_position_food(self):
        self.dot_turtle.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))


class Score(Turtle):
    score_turtle = Turtle()
    score = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"SCORE : {self.score}", align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE : {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Arial", 15, "normal"))


# IMPORTING DONE OF ALL FUNCTIONS

turtles_list = []

# SCREEN SETTINGS
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake_temp = Snake()  # CREATES THE SNAKE BODY
snake_food = food.Food()  # CREATES THE FOOD IN THE SCREEN RANDOMLY
snake_score = Score()
snake_food.hideturtle()  # HIDING THE OBJECT TURTL, SO we can make the Class turtle use!

screen.listen()
screen.onkey(snake_temp.up, 'Up')
screen.onkey(snake_temp.left, 'Left')
screen.onkey(snake_temp.right, 'Right')
screen.onkey(snake_temp.down, 'Down')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake_temp.move(snake_score.score)  # MAKES THE SNAKE MOVE FORWARD

    # DETECTION OF THE FOOD
    if snake_temp.turtles_list[0].distance(snake_food.dot_turtle) < 15:
        snake_food.new_position_food()
        snake_score.increase_score()
        snake_temp.increase_snake_body()

    # DETECTION OF THE COLLISION WITH WALL
    # if (snake_temp.turtles_list[0].xcor() > 280) or (snake_temp.turtles_list[0].xcor() < -280) or (
    #         snake_temp.turtles_list[0].ycor() > 280) or (snake_temp.turtles_list[0].ycor() < -280):
    #     game_is_on = False
    #     snake_score.game_over()

    # DETECTION OF WALL AND SPAWING OF OPPOSITE SIDE
    if(snake_temp.turtles_list[0].xcor() > 280):
        y_cordinate = snake_temp.turtles_list[0].ycor()
        snake_temp.turtles_list[0].goto(-280, y_cordinate)

    elif(snake_temp.turtles_list[0].xcor() < -280):
        y_cordinate = snake_temp.turtles_list[0].ycor()
        snake_temp.turtles_list[0].goto(280, y_cordinate)

    elif(snake_temp.turtles_list[0].ycor() > 280):
        x_cordinate = snake_temp.turtles_list[0].xcor()
        snake_temp.turtles_list[0].goto(x_cordinate, -280)

    elif(snake_temp.turtles_list[0].ycor() < -280):
        x_cordinate = snake_temp.turtles_list[0].xcor()
        snake_temp.turtles_list[0].goto(x_cordinate, 280)

    for snake_check_pos in snake_temp.turtles_list:
        if snake_check_pos == snake_temp.turtles_list[0]:
            continue
        if snake_temp.turtles_list[0].distance(snake_check_pos) < 10:
            game_is_on = False

print("Thanks for Playing")
snake_score.game_over()
screen.exitonclick()
