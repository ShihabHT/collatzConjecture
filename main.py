# Collatz Conjecture
import turtle
from colour import Color

colorList = list(Color("blue").range_to(Color("red"), 100))
# for x in colorList:
#     print(str(x))

startX = 600
startY = 450
turnRightAngle = 5
turnLeftAngle = 5
travelLength = 8

turtle.bgcolor("black")
turtle.Screen().setup(1920, 1080)
turtle.Screen().setworldcoordinates(0, 0, 1920, 1080)

t = turtle.Turtle()
t.penup()
t.pensize(2)
turtle.tracer(0, 0)  # turtle.tracer(0, 0) turns animation off, gives fastest possible speed


def get_steps(num):
    t.setpos(startX, startY)
    t.setheading(90)
    t.pendown()
    count = 0
    colorIndex = 0
    t.pencolor(str(colorList[colorIndex]))
    while num != 1:
        if num % 2 == 0:
            t.right(turnRightAngle)
            t.forward(travelLength)
            num = num / 2
            count += 1
        else:
            t.left(turnLeftAngle)
            t.forward(travelLength)
            num = num * 3 + 1
            count += 1
            colorIndex += 1
            t.pencolor(str(colorList[colorIndex]))
        print(count)

    t.penup()
    return count


if __name__ == '__main__':
    stepsCount = 0
    for x in range(10000, 11000):
        print("Working on", x)
        steps = get_steps(x)
        if steps == 16:
            stepsCount += 1
            print(x, "takes", steps, "steps")

    print("Total 16 steps takes", stepsCount, "numbers")
    turtle.done()
