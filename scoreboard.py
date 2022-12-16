from turtle import Turtle
# Global variables
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')


class Scoreboard(Turtle):
    """
    Is an inheritance from the class Turtle capable of tracking the score of a game.

    ====Own Attributes:======
    - self.game_is_on: states whether the game should continue
    - self.score: tracks the score of the game

    ====Own Methods:=========
    - self.refresh()
    - self.increase_score()
    - self.reset()
    - self.end_game()
    """
    def __init__(self):
        super().__init__()
        self.game_is_on = True
        self.score = 0
        with open("Data/high_score.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.setposition(x=0, y=275)
        self.refresh()

    def refresh(self):
        """
        Changes the appearance of the scoreboard.
        """
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increases the scoreboard by 1.
        """
        self.score += 1
        self.refresh()

    def reset(self):
        """
        Records the new high score in 'high_score.txt' and restarts the score count for the next game
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Data/high_score.txt", 'w') as file:
                file.write(f"{self.score}")
        self.score = 0
        self.refresh()

    def end_game(self):
        """
        Turns the boolean game_is_on to 'False'
        """
        self.game_is_on = False
