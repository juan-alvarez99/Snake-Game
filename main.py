"""
Portfolio Repository
Created by: Juan Alvarez
Date: 11.12.2022
#100DaysOfCode #Day20 #Day21
Github: https://github.com/juan-alvarez99
Linkedin: https://www.linkedin.com/in/juan-alv/
========================================================================================================
This are the rules:
    - The snake is always moving forward
    - You can control the direction of the snake using the keyboard arrows
    - The snake cannot turn 180 degrees in one single move
    - The snake gets bigger the more pieces of food (white dots in the screen) it eats
    - If the snake hits the wall or its own tail the game is over
    - Press space to exit the game
Did you like it? You can play as many times as you want!
Enjoy!
========================================================================================================
"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")

# Turn off the animation.
screen.tracer(0)

# Set up the initial snake and the scoreboard. Make the first piece of food appear.
snake = Snake()
scoreboard = Scoreboard()
food = Food()

# The snake is moved with the keyboard arrows.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(scoreboard.end_game, "space")

while scoreboard.game_is_on:
    # Refresh the screen.
    screen.update()
    # A delay is needed in order to be able to see the changes on the screen,
    # otherwise, they would happen too fast to be seen.
    time.sleep(0.1)
    # The snake is always moving forward.
    snake.move()

    # Detect collision with food. The snake grows its body.
    if snake.head.distance(food) < 15:
        snake.grow()
        scoreboard.increase_score()
        food.random_spawn()

    # Detect collision with wall. Game Over.
    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail. Game Over.
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
