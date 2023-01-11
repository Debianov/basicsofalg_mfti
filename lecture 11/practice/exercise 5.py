def setPositionStatusInQueenGame(N, M):
	i = N - 1
	matrix = [[False] * M for _ in range(N)]
	matrix[-1][-1] = False
	for j in range(M - 1): # движение влево # TODO в отдельную функцию
		matrix[i][j] = True
	j = M - 1
	for i in range(N - 1): # движение вправо # TODO в отдельную функцию
		matrix[i][j] = True
	for j in range(M - 2, -1, -1): # поиск ближайших клеток по правильным траекториям движения
		for i in range(N - 2, -1, -1):
			matrix[i][j] = True if falseCellCanGo(matrix, i, j, N, M) else False
	for i in range(N):
		for j in range(M):
			print(matrix[i][j], end=" ") # TODO pprint
		print("\n", end='')

def falseCellCanGo(matrix, current_N, current_M, bound_N, bound_M):
	j = current_M
	for i in range(current_N + 1, bound_N): # движение вниз # TODO в отдельную
		if not matrix[i][j]:
			return True
	i = current_N
	for j in range(current_M + 1, bound_M): # движение вправо # TODO в отдельную
		if not matrix[i][j]:
			return True
	for (i, j) in zip(range(current_N + 1, bound_N), range(current_M + 1, bound_M)): # движение по диаг. # TODO в отдельную
		if not matrix[i][j]:
			return True
	return False

setPositionStatusInQueenGame(6, 6)