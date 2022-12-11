from turtle import Turtle
import random


class Food(Turtle):
    """
    This class is an inheritance from the class Turtle.
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        # The shape of each piece of food is half the normal size of a Turtle object
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.fillcolor('white')
        self.speed('fastest')
        self.random_spawn()

    def random_spawn(self):
        """
        Appears in a random position within the screen size, but leaving 30 pixels margin to each end.
        """
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.setposition(random_x, random_y)
