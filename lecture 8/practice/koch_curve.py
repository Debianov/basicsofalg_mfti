import turtle

turtle.speed(300)

def drawCurve(size, deep):
	if deep == 0:
		turtle.forward(size)
	else:
		newSize = size / 3
		newDeep = deep - 1
		drawCurve(newSize, newDeep)
		turtle.left(60)
		drawCurve(newSize, newDeep)
		turtle.right(120)
		drawCurve(newSize, newDeep)
		turtle.left(60)
		drawCurve(newSize, newDeep)	


drawCurve(300, 3)