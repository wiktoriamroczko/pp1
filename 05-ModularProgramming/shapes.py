def drawSquare(n,x,y):
    import turtle
    
    turtle.up()
    turtle.goto(x-330,y+280)
    turtle.down()
    turtle.speed(10)
    
    for _ in range(4):
        turtle.fd(n)
        turtle.rt(90)
        
def circle(r,x,y):
    import turtle
    
    turtle.up()
    turtle.color('purple')
    turtle.goto(x,y)
    turtle.down()
    turtle.circle(r)
    
def triangle(m,x,y):
    import turtle
    
    turtle.up()
    turtle.color('pink')
    turtle.goto(x,y)
    turtle.down()
    turtle.lt(120)
    for _ in range(3):
        turtle.lt(120)
        turtle.fd(m)
        
def star(x,y):
    import turtle
    
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.fillcolor('gold')
    turtle.begin_fill()
    
    for _ in range(5):
        turtle.fd(25)
        turtle.rt(120)
        turtle.fd(25)
        turtle.rt(-48)
    turtle.end_fill()
    
def black_square(m,x,y):
    import turtle
    
    turtle.up()
    turtle.goto(x-330,y+280)
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    
    for _ in range(4):
        turtle.fd(m)
        turtle.rt(90)
    turtle.end_fill()

def szach(m):
    
    x = 1
    y = 1
    for _ in range(4):
        for _ in range(4):
            drawSquare(m,x,y)
            black_square(m,x+m,y)
            x+=2*m
        x-=8*m
        y-=m
        
        for _ in range(4):
            black_square(m,x,y)
            drawSquare(m,x+m,y)
            x+=2*m
        x-=8*m
        y-=m