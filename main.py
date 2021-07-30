# Collatz Conjecture
import turtle

turtle.bgcolor("black")
turtle.Screen().setup(1500, 900)
turtle.Screen().setworldcoordinates(0, 0, 1500, 900)

t = turtle.Turtle()
t.penup()
t.setpos(500, 200)
t.pendown()
t.pencolor("pink")
t.pensize(5)
t.forward(200)


def get_steps(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            count += 1
        else:
            num = num * 3 + 1
            count += 1
    return count


if __name__ == '__main__':
    stepsCount = 0
    for x in range(1, 65537):
        steps = get_steps(x)
        if steps == 16:
            stepsCount += 1
            print(x, "takes", steps, "steps")

    print("Total 16 steps takes", stepsCount, "numbers")
    turtle.done()
