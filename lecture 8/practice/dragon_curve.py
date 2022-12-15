import turtle

turtle.speed(300)

def drawDragonCurve(length, deep, count):
	if deep == 0:
		turtle.forward(length) # 4, 6, 7, 8
	else:
		newDeep = deep - 1
		if count % 2 == 0:
			turtle.right(45) # 1, 2, 3
			drawDragonCurve(length, newDeep, count) # 1, 2, 3
			turtle.left(90) # 3, 2
			drawDragonCurve(length, newDeep, count + 1) # 3, 2
			turtle.right(45) # 3
		else:
			turtle.left(45) # 7 
			drawDragonCurve(length, newDeep, count + 1) # 7
			turtle.right(90) # 7
			drawDragonCurve(length, newDeep, count) # 7
			turtle.left(45)

drawDragonCurve(10, 10, 0)