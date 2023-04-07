from turtle import Turtle,Screen

SNAKE_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in SNAKE_POSITION:
            self.add_segment(position)


    def add_segment(self,position):
        snake = Turtle("square")
        snake.penup()
        snake.speed("fastest")
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def turn_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
        

    def turn_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
