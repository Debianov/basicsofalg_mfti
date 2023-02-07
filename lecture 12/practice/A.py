	# TODO сделаны не все задачи (перерыв от темы).

"""
Вам даны 2 координаты 2 клеток на шахматном поле. Нужно ответить на вопрос, можно ли попасть из одной клетки в другую за не более чем 2 хода конем. 
В случае, если попасть возможно, надо вывести количество ходов, за которое это можно сделать. Если попасть невозможно, следует вернуть -1.
"""

def reachByHorse(start_x, start_y, finish_x, finish_y):
	if start_x == finish_x and start_y == finish_y:
		return 0
	matrix = [[0] * (finish_y + 4) for _ in range(finish_x + 4)]
	(start_x, start_y, finish_x, finish_y) = (start_x - 1, start_y - 1,
	finish_x - 1, finish_y - 1)
	matrix[start_x][start_y] = 1

	if start_x > finish_x:
		direction = -1
		finish_x_for_range = finish_x - 1
	else:
		direction = 1
		finish_x_for_range = finish_x + 1

	check_steps = [(-2, 1), (1, -2), (2, -1), (-1, 2), (1, 2), (2, 1), (-2, -1),
	(-1, -2)]
	for (step_x, step_y) in check_steps:
		check_x = start_x + step_x
		check_y = start_y + step_y
		if (check_x, check_y) == (finish_x, finish_y):
			return 1
		if check_x > 0 and check_y > 0:
			try:
				matrix[check_x][check_y] = 1
			except IndexError:
				continue

	for x in range(start_x, finish_x_for_range, direction):
		for y in range(0, finish_y + 1):
			if matrix[x][y]:
				continue
			check_steps = [(-2, 1), (1, -2), (2, -1), (-1, 2), (1, 2), (2, 1), (-2, -1),
			(-1, -2)]
			check_cells = []
			for (step_x, step_y) in check_steps:
				try:
					if not x + step_x < 0 and not y + step_y < 0:
						check_cells.append(matrix[x + step_x][y + step_y])
				except IndexError:
					continue
			check_cells = list(set(check_cells))
			try:
				check_cells.remove(0)
			except ValueError:
				pass
			if check_cells:
				matrix[x][y] = 1 + min(check_cells)

	result = matrix[finish_x][finish_y]
	return result if result <= 2 and result > 0 else -1

enter = []
for _ in range(4):
	enter.append(int(input()))

print(reachByHorse(*enter))