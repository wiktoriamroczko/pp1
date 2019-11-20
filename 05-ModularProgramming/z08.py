def drawSquare(x,y,n):
    import turtle
    
    turtle.up()
    turtle.goto(x-330,y+280)
    turtle.down()
    
    for i in range(4):
        turtle.fd(n)
        turtle.rt(90)

    
x = 1
y = 1
for j in range(4):
    for i in range(4):
        print(drawSquare(x,y,50))
        x+=50
    x-=200
    y-=50         
