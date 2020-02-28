from turtle import *

myTurtle = Turtle()

myTurtle.color('red', 'yellow')
myTurtle.begin_fill()
myTurtle.speed(0)
while True:
    myTurtle.forward(200)
    myTurtle.left(170)
    if abs(myTurtle.pos()) < 1:
        break
myTurtle.end_fill()
done()
