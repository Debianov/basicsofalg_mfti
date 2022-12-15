import turtle

def drawCantorSet(size, deep, x=0, y=0):
	newSize = size / 3
	if deep == 0:
		turtle.penup()
		turtle.goto(x, y)
		turtle.pendown()
		turtle.forward(size)
	else:
		drawCantorSet(newSize, deep - 1, x, y - 20)
		drawCantorSet(newSize, deep - 1, x + newSize * 2, y - 20)
		turtle.penup()
		turtle.goto(x, y)
		turtle.pendown()
		turtle.forward(size)

drawCantorSet(300, 1)
input()