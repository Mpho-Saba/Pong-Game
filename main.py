#This is the pong game
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreBoard import ScoreBoard

def main():
    screen = Screen()
    ball = Ball()
    score = ScoreBoard()
    r_paddle = Paddle((280, 0))
    l_paddle = Paddle((-280, 0))
    screen.screensize(800, 800)
    screen.bgcolor("black")
    screen.title("Lethal Pong")

    screen.tracer(0)  # turns off animation

    screen.listen()
    screen.onkey(r_paddle.goUp, "Up")
    screen.onkey(r_paddle.goDown, "Down")

    screen.onkey(l_paddle.goUp, "w")
    screen.onkey(l_paddle.goDown, "s")

    game_is_on = True

    while (game_is_on):
        ball.move()
        screen.update()
        time.sleep(ball.move_speed)

        #detect collision with wall
        if(ball.ycor() > 380 or ball.ycor() < -380):
            ball.bounce_y()

        #detect collision with paddle
        if(ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) and ball.xcor() < -320):
            ball.bounce_x()

        if(ball.xcor() > 380):
            ball.reset_position()
            score.l_point()

        if (ball.xcor() < -380):
            ball.reset_position()
            score.r_point()

    screen.exitonclick()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
