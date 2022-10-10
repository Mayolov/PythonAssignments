import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(1000):
    alex.speed(700)
    alex.forward(150 + i/20)
    alex.right(20+i/8)
    alex.forward(30)
    alex.left(200-i/8)

wn.exitonclick()