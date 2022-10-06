import turtle

turtle.left(90)

numberWings = 10

for R in range(1, 101, numberWings + 1):
	turtle.circle(R)

for R in range(-1, -101, numberWings + 1):
	turtle.circle(R)

turtle.done()