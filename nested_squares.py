import turtle
import math

def draw(length):
	for _ in range(4):
		turtle.left(90)
		turtle.forward(length)

def evaluationSquare(R):
	length = R * math.sqrt(2)
	return length

def moveToStartPosition(futureSquareSideLength, currentSquareSideLength):
	turtle.penup()
	turtle.right(90)
	turtle.forward((futureSquareSideLength - currentSquareSideLength) / 2)
	turtle.left(90)
	turtle.forward((futureSquareSideLength - currentSquareSideLength) / 2)
	turtle.pendown()

def evaluation():
	R = 30
	distanceBetweenPolygons = 10
	oldSquareSideLength = 0
	currentSquareSideLength = 0
	while True:
		currentSquareSideLength = evaluationSquare(R)
		if oldSquareSideLength:
			moveToStartPosition(currentSquareSideLength, oldSquareSideLength)
		draw(currentSquareSideLength)
		oldSquareSideLength = currentSquareSideLength
		R += distanceBetweenPolygons

evaluation()