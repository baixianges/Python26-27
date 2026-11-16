import turtle
bob=turtle.Turtle()

def rectangle(x,y,width,height,color):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    bob.fillcolor(color)
    bob.begin_fill()

    for times in range(2):
        bob.forward(width)
        bob.left(90)
        bob.forward(height)
        bob.left(90)

    bob.end_fill()

def star(x,y,size):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    bob.pencolor("yellow")
    bob.fillcolor("yellow")
    bob.begin_fill()

    for times in range(5):
        bob.forward(size)
        bob.right(144)

    bob.end_fill()

def mountain(x,y,size,color):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    bob.pencolor(color)
    bob.fillcolor(color)
    bob.begin_fill()
    
    bob.goto(x+size/2,y+size)
    bob.goto(x+size,y)
    bob.goto(x,y)
    
    bob.end_fill()

def tree(x,y):
    rectangle(x,y,12,45,"brown")

    bob.penup()
    bob.goto(x-30,y+30)
    bob.pendown()
    bob.pencolor("darkgreen")
    bob.fillcolor("darkgreen")
    bob.begin_fill()

    bob.goto(x+6,y+120)
    bob.goto(x+42,y+30)
    bob.goto(x-30,y+30)

    bob.end_fill()

def house (x,y):
    rectangle(x,y,140,110,"wheat")

    bob.penup()
    bob.goto(x-15,y+110)
    bob.prndown()
    bob.pencolor("brown")
    bob.fillcolor("brown")
    bob.begin_fill()

    bob.goto(x+70,y+170)
    bob.goto(x+155,y+110)
    bob.goto(x-15,y+110)

    bob.end_fill()
    rectangle(x+55,y,35,65,"saddlebrown")
    rectangle(x+15,y+65,30,30,"lightyellow")
    rectangle(x+100,y+65,30,30,"lightyellow")

