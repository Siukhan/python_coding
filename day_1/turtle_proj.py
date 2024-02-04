# The following code creates a turtle object, sets its properties (size, color, etc.), 
# and then uses a loop to move the turtle and draw a dodecagon shape.
# The turtle starts at the center of the canvas and moves forward by 100 units, 
# then turning 30 degrees to the right after each step. 
# After completing the loop, the turtle is hidden, 
# and the program waits for the user to click on the canvas before exiting.

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