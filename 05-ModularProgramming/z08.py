def drawSquare(x,y,n):
    import turtle
    
    turtle.setheading(0)
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(n)
        turtle.right(90)
        
        

x = 1
y = 1
for j in range(4):
    for i in range(4):
        print(drawSquare(x,y,50))
        x+=50
    x-=200
    y-=50
    