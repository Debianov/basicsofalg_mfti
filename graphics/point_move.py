import graphics as gr
import time

SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(200, 200)
velocity = gr.Point(1, -2)
acceleration = gr.Point(0, 0.1)

def add(point_1, point_2):
	new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
	return new_point

def draw_circle(coords):
	circle = gr.Circle(coords, 10)
	circle.setFill('red')
	circle.draw(window)

def clear_window():
	rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
	rectangle.setFill('green')
	rectangle.draw(window)

def check_coords(coords, velocity):
	if coords.x < 0 or coords.x > SIZE_X:
		velocity.x = -velocity.x
	if coords.y < 0 or coords.y > SIZE_Y:
		velocity.y = -velocity.y

def update_velocity(velocity, acceleration):
   return add(velocity, acceleration)

while True:
	clear_window()
	draw_circle(coords)
	coords = add(coords, velocity)
	check_coords(coords, velocity)
	time.sleep(0.1)