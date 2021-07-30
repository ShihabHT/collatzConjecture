# Collatz Conjecture
import turtle

turtle.bgcolor("black")
turtle.Screen().setup(1500, 900)
turtle.Screen().setworldcoordinates(0, 0, 1500, 900)

t = turtle.Turtle()
t.penup()
t.pencolor("pink")
t.pensize(5)


def get_steps(num):
    t.setpos(500, 200)
    t.setheading(90)
    t.pendown()
    count = 0
    while num != 1:
        if num % 2 == 0:
            t.right(10)
            t.forward(20)
            num = num / 2
            count += 1
        else:
            t.left(10)
            t.forward(20)
            num = num * 3 + 1
            count += 1

    t.penup()
    return count


if __name__ == '__main__':
    stepsCount = 0
    # for x in range(1, 65537):
    #     steps = get_steps(x)
    #     if steps == 16:
    #         stepsCount += 1
    #         print(x, "takes", steps, "steps")

    stepsTaken = get_steps(64)
    print(stepsTaken, "steps taken")
    stepsTaken = get_steps(128)
    print(stepsTaken, "steps taken")

    # print("Total 16 steps takes", stepsCount, "numbers")
    turtle.done()
