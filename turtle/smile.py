# TODO Здесь бы ООП не помешало. Ну и рассчётов добавить побольше.

import turtle

borders = []

def drawCircle(R, extent=360, colorPen=None, colorFill=None, cycles=1, fixBorders=False):
	if colorPen:
		turtle.pencolor(colorPen)
	turtle.pendown()
	if colorFill:
		turtle.fillcolor(colorFill)
		turtle.begin_fill()
	for _ in range(cycles):
		turtle.circle(R, extent=extent)
		if fixBorders:
			borders.append(turtle.position())
	turtle.penup()
	if colorFill:
		turtle.end_fill()

def drawLine(length, color=None, pensize=None):
	if color:
		turtle.color(color)
	turtle.pensize(pensize)
	turtle.pendown()
	turtle.forward(length)
	turtle.penup()

def drawFace():
	drawCircle(R=100, extent=90, colorFill="yellow", cycles=4, fixBorders=True)

def drawEyes():
	(topX, topY) = borders[1]
	startPositionLeftEyeX = topX - 30
	startPositionRigthEyeX = topX + 30
	startPositionEyesY = topY - 50
	turtle.setpos(startPositionLeftEyeX, startPositionEyesY)
	drawCircle(R=10, colorFill="blue")
	turtle.setpos(startPositionRigthEyeX, startPositionEyesY)
	drawCircle(R=10, colorFill="blue")

def drawNose():
	(topX, topY) = borders[1]
	startPositionNoseX = topX
	startPositionNoseY = topY - 50
	turtle.setpos(startPositionNoseX, startPositionNoseY)
	turtle.right(90)
	drawLine(length=60, color="black", pensize=10)

def drawMouth():
	(bottomX, bottomY) = borders[3]
	startPositionMouthX = bottomX - 50
	startPositionMouthY = bottomY + 80
	turtle.setpos(startPositionMouthX, startPositionMouthY)
	drawCircle(R=50, extent=180, colorPen="red")

drawFace()
drawEyes()
drawNose()
drawMouth()

turtle.done()