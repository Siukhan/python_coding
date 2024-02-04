import turtle

canvas = turtle.Screen()

pen = turtle.Turtle()
pen.pensize(3)
pen.pencolor('magenta')
pen.turtlesize(2)

for _ in range(12):
    pen.forward(100)
    pen.right(30) # 360/10 = 30

pen.hideturtle()
canvas.exitonclick()