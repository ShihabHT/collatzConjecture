# Collatz Conjecture
import turtle

startX = 1000
startY = 100
turnRightAngle = 15
turnLeftAngle = 25
travelLength = 6

turtle.bgcolor("black")
turtle.Screen().setup(1920, 1080)
turtle.Screen().setworldcoordinates(0, 0, 1920, 1080)

t = turtle.Turtle()
t.penup()
t.pencolor("blue")
t.pensize(4)
turtle.tracer(2, 0)


def get_steps(num):
    t.setpos(startX, startY)
    t.setheading(90)
    t.pendown()
    count = 0
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

    t.penup()
    return count


if __name__ == '__main__':
    stepsCount = 0
    for x in range(10000, 10100):
        print("Working on", x)
        steps = get_steps(x)
        if steps == 16:
            stepsCount += 1
            print(x, "takes", steps, "steps")
        print(x, "Takes", steps, "steps\n")

    print("Total 16 steps takes", stepsCount, "numbers")
    turtle.done()
