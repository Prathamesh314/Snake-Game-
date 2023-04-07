import turtle
import time
import snake_class
from snake_game_food import Food
from scoreboard_snake_game import ScoreBoard
snake = snake_class.Snake()
snake.create_snake()
food = Food()
score_board = ScoreBoard()
screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(fun=snake.turn_left,key="Left")
    screen.onkey(fun=snake.turn_right,key="Right")
    screen.onkey(fun=snake.up,key="Up")
    screen.onkey(fun=snake.down,key="Down")
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase()
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290:
        score_board.game_over()
        game_is_on = False
    elif snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        score_board.game_over()
        game_is_on = False
    
    for segments in snake.segments[1:]:
        if snake.segments[0].distance(segments) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()









