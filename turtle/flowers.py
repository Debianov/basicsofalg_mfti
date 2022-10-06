import turtle

def draw():
	turtle.circle(100)
	turtle.circle(-100)

numberPetals = 6

for _ in range(numberPetals):
	draw()
	turtle.right(360 / (numberPetals * 2))

turtle.done()