from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.color('white')
        self.write(f"Score: {self.score}",move=False,align='center',font=("Book Antiqua",20,"bold"))

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",move=False,align='center',font=("Book Antiqua",20,"bold"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over!!",move=False,align='center',font=("Book Antiqua",20,"bold"))
        self.goto(0,25)
        self.write(f"Your score : {self.score}",align='center',font=("Book Antiqua",20,"bold"))