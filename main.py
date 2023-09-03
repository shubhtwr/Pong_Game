from turtle import Screen
from paddle import Paddle
from ball import Ball
from game_over import Game

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
game = Game()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_dn, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_dn, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    elif ball.xcor() > 390:
        ball.reset_pos()
        game.left_point()
        # game_on = False
        # game.game_over(1)

    elif ball.xcor() < -390:
        ball.reset_pos()
        game.right_point()
        # game_on = False
        # game.game_over(2)

screen.exitonclick()
