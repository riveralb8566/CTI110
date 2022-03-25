import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(5)            
t.pencolor("red")     
t.shape("turtle")


t.forward(50)          
t.left(90)             
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.penup()
t.forward(90)
t.pendown()

t.left(90)
t.forward(100)          
t.left(120)            
t.forward(100)
t.left(120)
t.forward(100)

t.penup()
t.forward(90)
t.left(30)
t.pendown()


win.mainloop() 
