from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Game(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-300, 280)
        self.write(f"Score:{self.l_score}", align="center", font=FONT)
        self.goto(300, 280)
        self.write(f"Score:{self.r_score}", align="center", font=FONT)

    def game_over(self, player):
        self.write(f"Game Over! Player {player} loses.", align="center", font=FONT)

    def right_point(self):
        self.r_score += 1
        self.update()

    def left_point(self):
        self.l_score += 1
        self.update()


