import turtle

def draw():
	turtle.circle(radius=50, steps=6)
	turtle.circle(radius=-50, steps=6)

turtle.left(180)

n = 11
angle = 180 / n - 180

for _ in range(n):
	turtle.forward(200)
	turtle.left(angle)

turtle.done()