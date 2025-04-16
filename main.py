from turtle import Screen,Turtle
from snake import Snake
import time

screen=Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(600,600)
screen.tracer(0)
screen.listen()


snake=Snake()

screen.onkey(snake.up,"Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")



game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()





screen.exitonclick()
