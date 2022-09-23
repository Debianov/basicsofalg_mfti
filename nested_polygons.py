import turtle
import math

def draw(numAngles, polygonSideLength):
	turtle.pendown()
	angle = 360 / numAngles
	for _ in range(numAngles):
		turtle.left(angle)
		turtle.forward(polygonSideLength)
	turtle.penup()

def evaluation():
	startNumAngles = 3
	R = 10
	distanceBetweenPolygons = 10
	while True:
		polygonSideLength = 2 * R * math.sin(math.pi / startNumAngles)		
		x = (180 - 360 / startNumAngles) / 2 # Этот угол нужен для точки входа. А ещё из-за неё квадраты выглядят как ромбы.
		#! Для того, чтобы понять, почему применяется именно эта формула выше, нужно посмотреть прорисовку первой фигуры в замедленной скорости.
		turtle.left(x) # входим в позицию
		draw(startNumAngles, polygonSideLength)
		turtle.right(x) # выходим из позиции
		turtle.forward(distanceBetweenPolygons)
		startNumAngles += 1
		R += distanceBetweenPolygons

evaluation()