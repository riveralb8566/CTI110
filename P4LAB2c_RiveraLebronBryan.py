import turtle
win = turtle.Screen()
snow = turtle.Turtle()

snow.pensize(5)            
snow.pencolor("blue")     
snow.shape("turtle")

for i in range(10):
    for i in range(2):
        snow.forward(100)
        snow.right(60)
        snow.forward(100)
        snow.right(120)
    snow.right(36)
    


win.mainloop() 
