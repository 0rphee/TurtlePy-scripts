import turtle
import numpy
import pyautogui
import pygetwindow
from PIL import Image
import mss
import mss.tools


path = "/Users/roger/Desktop/pymages/"

primes = [i for i in range(900)]
angles = [numpy.degrees(i) for i in primes]

turtle.setup(1.0, 1.0)
turtle.hideturtle()
turtle.speed(0)
turtle.delay(0)


for prime, angle in zip(primes, angles):
    turtle.setheading(angle)
    turtle.forward(prime)
    turtle.goto(0, 0)

    title = "Python Python Turtle Graphics"
    x, y, width, height = (pygetwindow.getWindowGeometry(title))
    region = {'top': y+28, 'left': x, 'width': width, 'height': height-28}
    print(region)

    with mss.mss() as sct:
        # Grab the data
        img = sct.grab(region)

        # Save to the picture file
        mss.tools.to_png(img.rgb, img.size, output=path+str(prime)+".png")

turtle.exitonclick()