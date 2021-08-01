# Collatz Conjecture
import turtle
from colour import Color

colorList = list(Color("blue").range_to(Color("red"), 100))

startX = 50
startY = 50
turnRightAngle = 5
turnLeftAngle = 5
travelLength = 8

display_width = 1920
display_height = 1080

turtle.bgcolor("black")
turtle.Screen().setup(display_width, display_height)
turtle.Screen().setworldcoordinates(0, 0, display_width, display_height)

t = turtle.Turtle()
t.penup()
t.pensize(2)
turtle.tracer(1, 0)  # turtle.tracer(0, 0) turns animation off, gives fastest possible speed


def create_x_axis():
    t.pencolor("pink")
    t.setpos(startX, startY)
    t.pendown()
    x_axis_length = display_width - startX-50
    print("xAxisLength", x_axis_length)
    each_section = int(x_axis_length/10)
    print("eachSection", each_section)
    for section in range(startX+each_section, display_width-49, each_section):
        t.goto(section-(each_section/2), startY)
        t.goto(section-(each_section/2), startY+10)
        t.goto(section-(each_section/2), startY)
        t.goto(section, startY)
        t.goto(section, startY+10)
        t.goto(section, startY)
    t.penup()


def create_y_axis():
    t.pencolor("pink")
    t.setpos(startX, startY)
    t.pendown()
    y_axis_length = display_height - startY-50
    print("xAxisLength", y_axis_length)
    each_section = int(y_axis_length/5)
    print("eachSection", each_section)
    for section in range(startY+each_section, display_height-49, each_section):
        t.goto(startX, section-(each_section/2))
        t.goto(startX+10, section-(each_section/2))
        t.goto(startX, section-(each_section/2))
        t.goto(startX, section)
        t.goto(startX+10, section)
        t.goto(startX, section)
    t.penup()


def get_steps(num):
    t.setpos(startX, startY)
    t.setheading(90)
    t.pendown()
    count = 0
    color_index = 0
    t.pencolor(str(colorList[color_index]))
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
            color_index += 1
            t.pencolor(str(colorList[color_index]))
        print(count)

    t.penup()
    return count


if __name__ == '__main__':
    create_x_axis()
    create_y_axis()
    print("done")
    turtle.done()

    # stepsCount = 0
    # for x in range(1000, 1100):
    #     print("Working on", x)
    #     steps = get_steps(x)
    #     if steps == 16:
    #         stepsCount += 1
    #         print(x, "takes", steps, "steps")
    # print("Total 16 steps takes", stepsCount, "numbers")
