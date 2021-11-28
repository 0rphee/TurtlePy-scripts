import turtle
import math

turtle.radians()
turtle.speed(0)
turtle.delay(0)
turtle.setup(1.0, 1.0)
length = 500


def get_equivalent(max, x) -> float:
    return round(x / max, 3)


def get_xy(h):
    x = h * math.cos(h)
    y = h * math.sin(h)
    return (x, y)


def get_distance(cur, nex):
    x1, y1 = cur
    x2, y2 = nex
    x = x2 - x1
    y = y2 - y1
    distance = math.sqrt(x ** 2 + y ** 2)
    return distance


coords = [get_xy(h) for h in range(length)]
distances = [get_distance(cur, nex) for cur, nex in zip(coords[0:-1], coords[1:])]


for coord, distance in zip(coords, distances):
    angle = turtle.towards(coord)
    micro_angle = angle / 10
    micro_distance = distance / 10

    # for i in range(10):
    #     turtle.left(micro_angle)
    #     turtle.forward(micro_distance)
    turtle.right(angle)
    turtle.forward(10)
    turtle.forward(-20)
    turtle.forward(10)
    turtle.goto(coord)
turtle.exitonclick()

# m = y/x
#