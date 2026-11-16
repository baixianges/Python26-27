from myFunctions import*
bob.speed(0)
turtle.bgcolor("blue")

#star
for times in range(7):
    star(-330+times*100,200,22)

for times in range(6):
    star(-280+times*110,130,12)

#Moon
    bob.penup()
    bob.goto(240,180)
    bob.pendown()
    bob.pencolor("yellow")
    bob.fillcolor("yellow")
    bob.begin_fill()
    bob.circle(40)
    bob.end_fill()

#Mountain
mountain(-400,-100,300,"darkseagreen")
mountain(-170,-100,330,"seagreen")
mountain(80,-100,320,"darkseagreen")

#Ground
rectangle(-400,-300,800,200,"forestgreen")

#Tree
tree(-330,-180)
tree(-260,-180)
tree(230,-180)
tree(310,-180)

#House
house(-70,-180)

#Path
bob.penup()
bob.goto(-15,-180)
bob.pendown()
bob.pencolor("tan")
bob.goto(-40,-230)
bob.goto(-90,-300)

bob.hideturtle()
turtle.done()
