from turtle import Turtle


class Scoreboard(Turtle):
 
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.goto(0,280)
    self.score = 0
    #self.pendown()
    self.text = f"Score: {self.score}"
    self.pencolor("white")
    self.write(f"Score: {self.score}", align = "center")
    
  
  def increase_score(self):
    self.clear()
    self.score += 1
    self.write(f"Score: {self.score}", align = "center")

  def game_over(self):
    self.goto(0,0)
    self.write("Game Over", align = "center") 