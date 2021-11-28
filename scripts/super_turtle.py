import turtle
import math

turtle.speed(0)
turtle.delay(0)

for i in range(1000):
    turtle.forward(math.sin(i)*10%i)
    turtle.left(math.cos(i)*5)