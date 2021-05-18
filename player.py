from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Initialize the player"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def go_up(self):
        """Allow the player to move forward"""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Send the player back to the starting position"""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if player has crossed the finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False