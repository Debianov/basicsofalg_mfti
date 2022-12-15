import turtle

turtle.speed(300)

def drawLeviCurve(size, deep):
	if deep == 0:
		turtle.forward(size)
	else:
		newDeep = deep - 1
		turtle.left(45)
		drawLeviCurve(size, newDeep)
		turtle.right(90)
		drawLeviCurve(size, newDeep)
		turtle.left(45)

drawLeviCurve(70, 4)