"""
Авторский второй вариант решения.
"""

from pyrob.api import *
from decimal import *

def squareSizeEvaluation():
	squareLength = 1 
	squareWidth = 1
	while not wall_is_beneath():
		move_down()
		squareLength += 1
		squareWidth += 1
	move_up(squareLength - 1) # возврат в начальную позицию.
	return (squareLength, squareWidth)

def squareMiddleEvaluation(squareLength):
	middleSquare = Decimal(squareLength) / Decimal(2)
	middleSquare = int(middleSquare.quantize(Decimal('1.'), rounding=ROUND_HALF_UP))
	return middleSquare

def draw(squareLength, squareWidth, middleSquare):
	for stringNumber in range(squareWidth):
		if stringNumber == middleSquare:
			notFillCell = middleSquare
		else:
			notFillCell = stringNumber
		for cellPosition in range(squareLength):
			if not cellPosition == notFillCell and not cellPosition == (squareLength - notFillCell) - 1:
				fill_cell()
			if not stringNumber % 2 == 0 and not wall_is_on_the_left():
				move_left()
			elif stringNumber % 2 == 0 and not wall_is_on_the_right():
				move_right()
		if stringNumber == (squareWidth - 1): 
			move_left(squareLength - 1) # если последняя строка, то вернуть к точке в левой части.
		else:
			move_down() # иначе перейти на следующую строку.

@task(delay=0.01)
def task_9_3():
	(squareLength, squareWidth) = squareSizeEvaluation()
	middleSquare = squareMiddleEvaluation(squareLength)
	draw(squareLength, squareWidth, middleSquare)

if __name__ == '__main__':
	run_tasks()