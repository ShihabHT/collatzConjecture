# Collatz Conjecture
import turtle
from colour import Color

colorList = list(Color("blue").range_to(Color("red"), 50))

display_width = 1920
display_height = 1080

startX = 50
startY = 70
x_axis_padding = 50
y_axis_padding = 30

x_axis_steps = 120
y_axis_steps = 9500
x_axis_multiplier = (display_width-startX-x_axis_padding) / x_axis_steps
y_axis_multiplier = (display_height-startY-y_axis_padding) / y_axis_steps

turtle.bgcolor("black")
turtle.Screen().setup(display_width, display_height)
turtle.Screen().setworldcoordinates(0, 0, display_width, display_height)

t = turtle.Turtle()
t.penup()
t.pensize(2)
t.pencolor("#49FF00")
turtle.tracer(1, 0)  # turtle.tracer(0, 0) turns animation off, gives fastest possible speed


def create_x_axis():
    t.setpos(startX, startY-20)
    t.write("(0, 0)", align="center")
    t.setpos(startX, startY)
    t.pendown()
    x_axis_length = display_width - startX-x_axis_padding
    print("xAxisLength", x_axis_length)
    each_section = int(x_axis_length/10)
    print("eachSection", each_section)
    each_steps = x_axis_steps / 10
    step_count = 1
    for section in range(startX+each_section, display_width-x_axis_padding+1, each_section):
        t.goto(section-(each_section/2), startY)
        t.goto(section-(each_section/2), startY+10)
        t.goto(section-(each_section/2), startY)
        t.goto(section, startY)
        t.penup()
        t.goto(section, startY-20)
        t.write(int(each_steps*step_count), align="center")
        step_count += 1
        t.goto(section, startY)
        t.pendown()
        t.goto(section, startY+10)
        t.goto(section, startY)
    t.penup()


def create_y_axis():
    t.setpos(startX, startY)
    t.pendown()
    y_axis_length = display_height - startY-y_axis_padding
    print("xAxisLength", y_axis_length)
    each_section = int(y_axis_length/10)
    print("eachSection", each_section)
    each_steps = y_axis_steps / 10
    step_count = 1
    for section in range(startY+each_section, display_height-y_axis_padding+1, each_section):
        t.goto(startX, section)
        t.penup()
        t.goto(startX-20, section-8)
        t.write(int(each_steps*step_count), align="center")
        step_count += 1
        t.goto(startX, section)
        t.pendown()
        t.goto(startX+10, section)
        t.goto(startX, section)
    t.penup()


def get_steps(num):
    t.setpos(startX, startY+num*y_axis_multiplier)
    t.setheading(90)
    t.pendown()
    operation_count = 0
    color_index = 0
    peak = num
    t.pencolor(str(colorList[color_index]))
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            operation_count += 1
            t.goto(startX+operation_count*x_axis_multiplier, startY+(num*y_axis_multiplier))
        else:
            num = num * 3 + 1
            operation_count += 1
            color_index += 1
            if num > peak:
                peak = num
            t.goto(startX+operation_count*x_axis_multiplier, startY+(num*y_axis_multiplier))
            t.pencolor(str(colorList[color_index]))
            t.write(int(num), align='center')

    t.penup()
    return operation_count, int(peak)


if __name__ == '__main__':
    create_x_axis()
    create_y_axis()

    for x in range(100, 200):
        steps, peak_value = get_steps(x)
        print(x, "takes", steps, "steps and the peak value is", peak_value)

    print("\nProcess Finished!")
    # get_steps(633)  # for testing if it matches 1900 in y axis, y_axis_multiplier
    # get_steps(55)
    # get_steps(27)
    turtle.done()
