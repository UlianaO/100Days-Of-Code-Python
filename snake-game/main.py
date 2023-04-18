# My version of the most popular Snake Game
from turtle import Turtle, Screen
from Snake import Snake
import time
from Food import Food
from Scoreboard import Scoreboard

# Screen defaults
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightsteelblue1")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()  # once triggered, calls create-snake()
food = Food()
scoreboard = Scoreboard()

# Connect arrows keystrokes on keyboard to the snake`s movement
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")  # move_up triggers when arrow Up is clicked
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

# when screen is updated after manipulations, the user can not see the manipulations themselves
screen.update()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 18:  # if snake`s head is 15 pixels away from the food
        food.refresh_food()
        scoreboard.update_score()
        snake.increase_size()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_game()
        snake.reset_snake()

    # Detect collision with tail, only can happen if 4 or more segments
    for segment in snake.full_snake[4:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_game()
            snake.reset_snake()

screen.exitonclick()