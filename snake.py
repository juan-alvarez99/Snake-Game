from turtle import Turtle
# Global variables
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    """
    =====Attributes:=====
    - self.body: a list containing all the segments that the Snake is made of
    - self.head: is the first element in the body list
    - self.tail: is the last element in the body list

    =====Methods:========
    - self.create_snake()
    - self.add_segment()
    - self.grow()
    - self.move()
    - self.up()
    - self.down()
    - self.left()
    - self.right()
    """
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.tail = self.body[-1]
        self.draw_screen_limits()

    def create_snake(self):
        """
        Adds the first three segments of the snake to the body.
        """
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, position):
        """
        Add a new segment to the snake body list at a specified position. Each new segment is a Turtle object.
        """
        snake_part = Turtle("square")
        snake_part.penup()
        snake_part.color("white")
        snake_part.setposition(position)
        self.body.append(snake_part)

    def grow(self):
        """
        Add a segment at the position of the current tail of the snake to make it bigger.
        """
        self.add_segment(self.tail.position())
        self.tail = self.body[-1]

    def move(self):
        """
        Each element in the body list goes to the position of the next segment starting from the last on the list:
        body[3] goes to the position of body[2], body[2] to body[1]'s position and so on.
        The head of the snake makes the last move and the rest of the body follows its way.
        """
        # First move the body following the head position
        for seg_number in range(len(self.body) - 1, 0, -1):
            new_position = self.body[seg_number - 1].position()
            self.body[seg_number].goto(new_position)
        # Then move the head
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for segment in self.body:
            segment.hideturtle()
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
        self.tail = self.body[-1]

    @staticmethod
    def draw_screen_limits():
        painter = Turtle()
        painter.hideturtle()
        painter.penup()
        painter.pencolor('white')
        painter.pensize(2)
        painter.goto(x=270, y=270)
        painter.pendown()
        painter.goto(x=270, y=-270)
        painter.goto(x=-270, y=-270)
        painter.goto(x=-270, y=270)
        painter.goto(x=270, y=270)

    def right(self):
        """
        Changes the heading of the snake's head rightwards.
        The snake cannot make a 180-degree turn.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        """
        Changes the heading of the snake's head upwards.
        The snake cannot make a 180-degree turn.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        """
        Changes the heading of the snake's head leftwards.
        The snake cannot make a 180-degree turn.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """
        Changes the heading of the snake's head downwards.
        The snake cannot make a 180-degree turn.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
