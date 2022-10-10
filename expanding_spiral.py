import turtle

a = turtle.Turtle()
for i in range(60):
    a.forward(10+i/4)
    a.right(30-i/12)

turtle.done()