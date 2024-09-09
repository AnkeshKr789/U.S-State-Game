from turtle import Turtle


class Locator(Turtle):
    def __init__(self, position, state):
        super().__init__()
        self.color("black")
        self.pensize(5)
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(f"{state}", align="center", font=("Arial", 10, "normal"))

    def reset(self):
        self.clear()
