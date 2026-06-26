import turtle
turtle.Screen().bgcolor('yellow')

#first triangle 
t = turtle.Turtle()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
#moving turtle to another location
t.penup()
t.right(150)
t.forward(50)
t.pendown()
#second triangle 
t.right(90)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
turtle.done()