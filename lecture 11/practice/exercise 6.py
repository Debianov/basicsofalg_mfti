# король, в отличии от ферзя, может передвигаться за 1 ход только на 1 клетку. Держу в курсе.

def setPositionsStatusInKingGame(N, M):
	i = N - 1
	matrix = [[False] * M for _ in range(N)]
	for j in range(M - 1, -1, -1): # поиск ближайших клеток по правильным траекториям движения
		for i in range(N - 1, -1, -1):
			matrix[i][j] = True if falseCellCanGo(matrix, i, j, N, M) else False
	for i in range(N):
		for j in range(M):
			print(matrix[i][j], end=" ") # TODO pprint
		print("\n", end='')

def falseCellCanGo(matrix, current_N, current_M, bound_N, bound_M):
	if current_N + 1 < bound_N: # TODO аналогично 5 заданию.
		j = current_M
		i = current_N + 1
		if not matrix[i][j]:
			return True
	if current_M + 1 < bound_M:
		i = current_N
		j = current_M + 1
		if not matrix[i][j]:
			return True
	if current_M + 1 < bound_M and current_N + 1 < bound_N:
		i = current_N + 1
		j = current_M + 1
		if not matrix[i][j]:
			return True
	return False

setPositionsStatusInKingGame(4, 5)