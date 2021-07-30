import turtle

turtle.bgcolor("black")
turtle.Screen().setup(1500, 900)
turtle.Screen().setworldcoordinates(0, 0, 1500, 900)

t = turtle.Turtle()
t.penup()
t.pencolor("pink")
t.pensize(5)

t.setpos(500, 200)
t.left(90)
t.pendown()
t.forward(100)
t.right(60)
t.penup()
t.setpos(500, 200)
t.setheading(90)
turtle.done()
