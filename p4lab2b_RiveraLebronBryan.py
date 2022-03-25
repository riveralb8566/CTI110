import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(5)            
t.pencolor("red")     
t.shape("turtle")

t.right(90)
t.back(100)
t.left(45)
t.forward(25)
t.right(70)
t.forward(45)
t.left(70)
t.forward(25)
t.right(75)
t.forward(35)


t.penup()
t.left(120)
t.forward(60)
t.left(90)
t.pendown()

t.forward(100)
t.left(45)
t.back(35)
t.left(90)
t.forward(35)
t.left(75)
t.forward(35)
t.right(25)
t.forward(20)

win.mainloop() 
