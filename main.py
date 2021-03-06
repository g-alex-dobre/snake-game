from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

time.sleep(5)
while game_is_on:
  screen.update()
  time.sleep(0.1)
  
  snake.move_snake()
#detect colision with food
  if snake.segments[0].distance(food) < 15:
    food.refresh()
    scoreboard.increase_score()
    snake.extend()

  #detect colision with wall
  if snake.segments[0].xcor()>280 or snake.segments[0].xcor()< -280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()< -280:
    game_is_on = False
    scoreboard.game_over()

  #detect collision with tail
  for segment in snake.segments:
    if snake.segments[0] == segment:
      pass
    elif snake.segments[0].distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()


screen.exitonclick()