from turtle import Turtle
# Global variables
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    """
    Is an inheritance from the class Turtle capable of tracking the score of a game.

    ====Own Attributes:======
    - self.game_is_on: states whether the game should continue
    - self.score: tracks the score of the game

    ====Own Methods:=========
    - self.refresh()
    - self.increase_score()
    - self.game_over()
    """
    def __init__(self):
        super().__init__()
        self.game_is_on = True
        self.score = 0
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.setposition(x=0, y=270)
        self.refresh()

    def refresh(self):
        """
        Changes the appearance of the scoreboard.
        """
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increases the scoreboard by 1.
        """
        self.score += 1
        self.clear()
        self.refresh()

    def game_over(self):
        """
        Shows that the game is over and turn self.game_is_on to False and thus the game stops.
        """
        self.setposition(x=0, y=0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.game_is_on = False
