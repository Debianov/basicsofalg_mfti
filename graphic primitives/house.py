import graphics as gr

project = gr.GraphWin("Вся работа выполнена шариковой ручкой", 1000, 1000)

def drawColoredBackround():
	separator1 = gr.Polygon(gr.Point(0, 0), gr.Point(0, 400), gr.Point(1000, 400), gr.Point(1000, 0))
	separator2 = gr.Polygon(gr.Point(0, 400), gr.Point(0, 1000), gr.Point(1000, 1000), gr.Point(1000, 400))
	separator1.setWidth(0)
	separator2.setWidth(0)
	separator1.setFill('blue')
	separator2.setFill(gr.color_rgb(255, 240, 245))
	separator1.draw(project)
	separator2.draw(project)

def drawHouse(centerX, centerY, width, length):
	stepY = width / 2
	stepX = length / 2
	house = gr.Polygon(gr.Point(centerX - stepX, centerY + stepY), gr.Point(centerX + stepX, centerY + stepY), gr.Point(centerX + stepX, centerY - stepY), 
	gr.Point(centerX - stepX, centerY - stepY))
	house.setWidth(5)
	house.setFill('brown')
	house.draw(project)

def drawWindow(centerX, centerY, width, length):
	stepY = width / 2
	stepX = length / 2
	window = gr.Polygon(gr.Point(centerX - stepX, centerY + stepY), gr.Point(centerX + stepX, centerY + stepY), gr.Point(centerX + stepX, centerY - stepY), 
	gr.Point(centerX - stepX, centerY - stepY))
	verticalWindowLine = gr.Line(gr.Point(centerX, centerY + stepY), gr.Point(centerX, centerY - stepY))
	horizontalWindowLine = gr.Line(gr.Point(centerX + stepX, centerY), gr.Point(centerX - stepX, centerY))
	window.setWidth(3)
	verticalWindowLine.setWidth(3)
	horizontalWindowLine.setWidth(3)
	window.setFill('yellow')
	window.draw(project)
	verticalWindowLine.draw(project)
	horizontalWindowLine.draw(project)

def drawClouds(x, y, radius):
	for iter in range(4):
		if iter % 2 == 0:
			cloud = gr.Circle(gr.Point(x, y), radius)
			y += 20
		else:
			cloud = gr.Circle(gr.Point(x, y), radius)
			y -= 20
		x += 20
		cloud.setFill('white')
		cloud.draw(project)	

drawColoredBackround()
drawHouse(550, 700, 300, 300)
drawWindow(550, 700, 200, 200)
drawClouds(120, 180, 20)
drawClouds(200, 260, 20)

project.getMouse()
project.close()