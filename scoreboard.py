#imports
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 225)
        self.level = 1 
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)

