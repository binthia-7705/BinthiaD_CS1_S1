from turtle import *
from random import *

sc=Screen()
bgcolor("#DEE2E6")
colormode(255)

pen1=Turtle()
pen1.speed(0)
pen1.hideturtle()

pen1.penup()
pen1.goto(0,-300)
pen1.pendown()
pen1.color("white")
pen1.begin_fill()
pen1.circle(300)
pen1.end_fill()

pen1.penup()
pen1.goto(-21,-100)
pen1.pendown()
pen1.color("#7F5539")
pen1.begin_fill()
for i in range(2):
    pen1.forward(50)
    pen1.right(90)
    pen1.forward(40)
    pen1.right(90)
pen1.end_fill()

y=-100
w=350
h=30

while w>50:
    w=w-30
    x=20-w/2
    pen1.color("#4F772D")
    pen1.penup()
    pen1.goto(x,y)
    pen1.pendown()
    pen1.begin_fill()
    for i in range(2):
        if i==0:
            pen1.forward(w)
            pen1.left(145)
        else:
            pen1.forward(w-50)
            pen1.left(35)
        pen1.forward(h+25)
        if i==0:
            pen1.left(35)
        else:
            pen1.left(145)
    pen1.end_fill()
    y=y+h

penup()
goto(-15,210)
pendown()
begin_fill()
color("yellow")
for i in range(5):
    forward(30)
    right(144)
end_fill()
hideturtle()

colors=["red","yellow","blue","pink","orange","palegreen","cyan","purple","darkorchid","azure"]
l1=Pen()
l1.hideturtle()
l1.up()
l1.setposition(-47,-67)
l1.down()

l2=Pen()
l2.hideturtle()
l2.up()
l2.setposition(-102,-41)
l2.down()

l3=Pen()
l3.hideturtle()
l3.up()
l3.setposition(-27,128)
l3.down()

l4=Pen()
l4.hideturtle()
l4.up()
l4.setposition(-26,28)
l4.down()

l5=Pen()
l5.hideturtle()
l5.up()
l5.setposition(67,-63)
l5.down()

l6=Pen()
l6.hideturtle()
l6.up()
l6.setposition(36,112)
l6.down()

l7=Pen()
l7.hideturtle()
l7.up()
l7.setposition(67,39)
l7.down()

penup()
goto(-180,-200)
color("red")
write("MERRY CHRISTMAS",font=("Courier New",30))
hideturtle()

m=0
while True:
    l1.dot(20,colors[m%10])
    l2.dot(20,colors[(m+1)%10])
    l3.dot(20,colors[(m+2)%10])
    l4.dot(20,colors[(m+3)%10])
    l5.dot(20,colors[(m+4)%10])
    l6.dot(20,colors[(m+5)%10])
    l7.dot(20,colors[(m+6)%10])
    m=m+1
    hideturtle() 
