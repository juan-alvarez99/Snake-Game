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
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()

    # Detect collision with tail. Game Over.
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()

screen.exitonclick()
