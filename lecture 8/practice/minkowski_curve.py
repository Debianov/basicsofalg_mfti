import turtle

turtle.speed(300)

def drawMinkowskiCurve(length, deep):
	if deep == 0:
		turtle.forward(length)
	else:
		newDeep = deep - 1
		drawMinkowskiCurve(length, newDeep)
		turtle.left(90)
		drawMinkowskiCurve(length, newDeep)
		turtle.right(90)
		drawMinkowskiCurve(length, newDeep)
		turtle.right(90)
		drawMinkowskiCurve(length * 2, newDeep)
		turtle.left(90)
		drawMinkowskiCurve(length, newDeep)
		turtle.left(90)
		drawMinkowskiCurve(length, newDeep)
		turtle.right(90)
		drawMinkowskiCurve(length, newDeep)

drawMinkowskiCurve(10, 2)