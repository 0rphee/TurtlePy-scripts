import turtle
from math import sin, radians as deg_rad
from random import randrange

turtle.colormode(255)
turtle.bgcolor(0, 0, 0)
turtle.delay(1)

print(turtle.pos())

turtle.goto(400, -30)

def new_rgb() -> list:
    while True:
        rgb = [randrange(1, 255) for _ in range(3)]
        valid = [i < 20 for i in rgb]
        if valid.count(True) <= 2:
            return rgb


def draw_line(size):
    turtle.pencolor(new_rgb())
    turtle.forward(size)


def shape(sides: int, size=50):
    degrees = 360 / sides
    inside_deg = (((sides - 2) * 180) / sides) / 2
    center_deg = (180 - (inside_deg * 2))
    x = 360 / (2 * sides)
    k = round(sin(deg_rad(x)), 4)
    radius = size / (2 * k)

    def draw_perimeter():
        for _ in range(sides):
            draw_line(size)
            turtle.right(degrees)

    def draw_inside_lines():
        for i in range(sides - 1):
            draw_line(radius)
            turtle.end_fill()
            turtle.fillcolor(new_rgb())
            turtle.begin_fill()
            draw_line(-radius)
            turtle.right(center_deg)
        draw_line(radius)
        turtle.end_fill()

    draw_perimeter()
    turtle.right(inside_deg)

    turtle.fillcolor(new_rgb())
    turtle.begin_fill()

    draw_line(radius)
    turtle.left(180 - center_deg)
    draw_inside_lines()
    turtle.right(inside_deg)


def main():
    for sides, side_sum, shape_sum in zip(range(3, 15), range(0, 60, 5), range(12)):
        shape(sides, 20 + side_sum)
        draw_line(30 + shape_sum ** 2.5)
    turtle.exitonclick()


if __name__ == "__main__":
    main()