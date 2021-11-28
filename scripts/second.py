import turtle
import math


def formula(x):
   try:
      return math.sqrt((math.tan(x))*100)
   except ValueError:
      return None

coords = [(x * 10, formula(x)) for x in range(-20, 20)]
turtle.penup()
try:
   turtle.goto(coords[0])
except TypeError:
   try:
      turtle.goto(coords[1])
   except TypeError:
      try:
         turtle.goto(coords[2])
      except TypeError:
         turtle.goto(coords[3])


turtle.pendown()
for i, coord in enumerate(coords):
   try:
      turtle.goto(coord)
   except TypeError:
      turtle.penup()
      try:
         turtle.goto(coords[i+1])
      except TypeError:
         try:
            turtle.goto(coords[i+2])
         except TypeError:
            try:
               turtle.goto(coords[i+3])
            except TypeError:
               turtle.goto(coords[i+4])
      turtle.pendown()

turtle.exitonclick()
