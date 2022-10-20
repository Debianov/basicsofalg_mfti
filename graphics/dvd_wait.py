	# TODO сделать нормальное закрытие.

import graphics as gr
import time

SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("DVD", SIZE_X, SIZE_Y)

currentPosition = gr.Point(200, 200)
currentSpeed = gr.Point(1, 2)

def generateLogo(point):
	logo = gr.Image(point, "dvd.gif")
	return logo

def updatePosition(point, newPoint):
	point.x += newPoint.x
	point.y += newPoint.y

def setBackground():
	blank = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
	blank.setFill("black")
	blank.draw(window)

def coordEditing(point, speed):
	if point.x < 30 or point.x > SIZE_X - 30:
		speed.x = -(speed.x)
	if point.y < 30 or point.y > SIZE_Y - 30:
		speed.y = -(speed.y)

setBackground()
logo = generateLogo(currentPosition)
logo.draw(window)
lastPosition = gr.Point(currentPosition.x, currentPosition.y)
while True:
	updatePosition(currentPosition, currentSpeed)
	coordEditing(currentPosition, currentSpeed)
	diffPosition = gr.Point(currentPosition.x - lastPosition.x, currentPosition.y - lastPosition.y)
	logo.move(diffPosition.x, diffPosition.y)
	lastPosition = gr.Point(currentPosition.x, currentPosition.y)
	time.sleep(0.01)