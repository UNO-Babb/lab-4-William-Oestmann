#TurtleGraphics.py
#Name:William Oestmann
#Date: 9/18/24
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(myTurtle, sides):
    for i in range(sides):
        myTurtle.forward(50)
        myTurtle.right(360 / sides)


def fillCorner(myTurtle, corner):
    drawSquare(myTurtle, 100) #square of size 100
    myTurtle.up()
    if corner == 1:
        myTurtle.goto(0,0)
    elif corner == 2:
        myTurtle.goto(50,0)
    elif corner == 3:
        myTurtle.goto(50,-50)
    elif corner == 4:
        myTurtle.goto(0,-50)
    myTurtle.down()
    myTurtle.begin_fill()
    drawSquare(myTurtle, 50)
    myTurtle.end_fill()


def squaresInSquares(myTurtle, number):
    x = 0
    y = 0
    size = 100
    for i in range(number):
        myTurtle.down()
        drawSquare(myTurtle, size)
        size = size - 10
        myTurtle.up()
        x = x + 5
        y = y - 5
        myTurtle.goto(x,y)
        


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
