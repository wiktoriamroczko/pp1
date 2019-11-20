import shapes

x=1
y=1
for j in range(4):
    for i in range(4):
        print(shapes.drawSquare(50,x,y))
        x+=50
    x-=4*50
    y-=50