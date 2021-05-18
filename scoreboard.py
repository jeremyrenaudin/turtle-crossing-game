from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    """Initialize the score board"""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        """Update the score board"""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Update the level displayed on the score board"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display GAME OVER message"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)