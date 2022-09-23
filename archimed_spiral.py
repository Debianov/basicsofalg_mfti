import turtle
import math

spiralLength = 5 # длина 1 спирали
k = spiralLength / (2 * math.pi) # какой-то "параметр спирали"; влияет на расстояние между линиями
step = 0 # шаг

while True:
	D = k * step #? прекрасно работает и без D на k в выражениях ниже. 
	x = D * math.cos(step) #?
	y = D * math.sin(step) #?
	turtle.goto(x, y)
	step += 0.1