from turtle import Turtle

class Snake():

  
  def __init__(self):  
    self.segments = []
    self.starting_position = [(0,0),(-20,0),(-40,0)]

    for position in self.starting_position:
      new_segment= Turtle("square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(position)
      self.segments.append(new_segment)

  def extend(self):
    new_segment= Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(self.segments[-1].xcor(),self.segments[-1].ycor())
    self.segments.append(new_segment)

  def move_snake(self, heading = 0):

    for i in range(len(self.segments)-1,0, -1):
      newx = self.segments[i-1].xcor()
      newy = self.segments[i-1].ycor()
      self.segments[i].goto(newx, newy)
    self.segments[0].forward(20)

  def up(self):
    if self.segments[0].heading() != 90 and self.segments[0].heading() != 270:
      self.segments[0].setheading(90)

  def down(self):
    if self.segments[0].heading() != 90 and self.segments[0].heading() != 270:
      self.segments[0].setheading(270)

  def left(self):
    if self.segments[0].heading() != 0 and self.segments[0].heading() != 180:
      self.segments[0].setheading(180)
  
  def right(self):
    if self.segments[0].heading() != 0 and self.segments[0].heading() != 180:
      self.segments[0].setheading(0)
