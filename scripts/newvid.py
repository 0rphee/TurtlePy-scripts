import math
import turtle

magnitude = 500

turtle.speed(0)
turtle.delay(0)
turtle.setup(1.0, 1.0)

def draw_wave(func, magnitude: int, amp: int, period):
    turtle.penup()

    for x in range(-magnitude, magnitude):
        if x == -magnitude:
            turtle.penup()
        y = amp * func(period * x)
        turtle.goto(x, y)
        if x == -magnitude:
            turtle.pendown()


for i in range(60, 151, 10):
    draw_wave(math.sin, magnitude, 100, 1 / i)
    draw_wave(math.cos, magnitude, 100, 1 / i)



turtle.exitonclick()