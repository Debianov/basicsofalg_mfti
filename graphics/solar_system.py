import graphics as gr
import time

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
ball_coords = gr.Point(400, 700)
sun_center = gr.Point(400, 400)
velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)

def add(point_1, point_2):
	new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
	return new_point

def sub(point_1, point_2):
	new_point = gr.Point(point_1.x - point_2.x, point_1.y - point_2.y)
	return new_point

def draw_sun():
	sun = gr.Circle(sun_center, 50)
	sun.setFill('yellow')
	sun.draw(window)

def generate_ball(coords):
	circle = gr.Circle(coords, 10)
	circle.setFill('red')
	return circle

def check_coords(coords, velocity):
	if coords.x < 0 or coords.x > SIZE_X:
		velocity.x = -velocity.x
	if coords.y < 0 or coords.y > SIZE_Y:
		velocity.y = -velocity.y

def update_coords(coords, velocity):
	return add(coords, velocity)

def update_velocity(velocity, acceleration):
	return add(velocity, acceleration)

def update_acceleration(ball_coords, center_coords):
	diff = sub(ball_coords, center_coords)
	distance = (diff.x ** 2 + diff.y ** 2) ** (3/2)
	G = 2000
	return gr.Point(-diff.x * G / distance, -diff.y * G / distance)

draw_sun()
ball = generate_ball(ball_coords)
ball.draw(window)
last_coord = ball_coords
while True:
	acceleration = update_acceleration(ball_coords, sun_center)
	velocity = update_velocity(velocity, acceleration)
	ball_coords = update_coords(ball_coords, velocity)
	check_coords(ball_coords, velocity)
	new_coords = sub(ball_coords, last_coord)
	ball.move(new_coords.x, new_coords.y)
	last_coord = ball_coords
	time.sleep(0.01)