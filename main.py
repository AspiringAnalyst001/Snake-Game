from turtle import Screen
from food import Food
from snake import Snake
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
screen.title("My Snake is Hungry")
screen.tracer(0)

snake = Snake()
food = Food()
sb = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        sb.increase()
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        sb.gameover()

    for segments in snake.Segment[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            sb.gameover()
screen.exitonclick()
