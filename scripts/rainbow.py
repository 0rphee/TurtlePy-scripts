import turtle
import math

turtle.colormode(255)
turtle.speed(0)
turtle.delay(0)
turtle.setup(1.0, 1.0)
turtle.width(1)
turtle.goto(-700,0)

freq = 0.03


def cube(size):
    x1, y1 = turtle.position()
    f_corner = (x1, y1-size)
    s_corner = (x1+size/50, y1-size)
    t_corner = (x1+size/50, y1)
    corners = (f_corner, s_corner, t_corner)

    turtle.begin_fill()
    for corner in corners:
        turtle.goto(corner)

    turtle.end_fill()


for i in range(500):
    red = round(math.sin(freq * i + 0) * 127 + 128)
    green = round(math.sin(freq * i + 2) * 127 + 128)
    blue = round(math.sin(freq * i + 4) * 127 + 128)
    rgb = (red, green, blue)

    turtle.pencolor(rgb)
    turtle.fillcolor(rgb)
    cube(50)


turtle.exitonclick()