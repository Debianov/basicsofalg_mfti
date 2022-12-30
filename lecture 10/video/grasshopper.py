def getJumpsToCell(N):
	cell_jumps = [0, 1] + [0] * N
	for ind in range(2, N + 1):
		cell_jumps[ind] = cell_jumps[ind - 1] + cell_jumps[ind - 2]
	return cell_jumps[N]

print(getJumpsToCell(6))

# прокаченная версия.
def getJumpsToCell(N, allowed_cells):
	cell_jumps = [0, 1, 1] + [0] * N
	for ind in range(3, N + 1):
		if allowed_cells[ind]:
			cell_jumps[ind] = cell_jumps[ind - 1] + cell_jumps[ind - 2] + cell_jumps[ind - 3]
	return cell_jumps[N]

print(getJumpsToCell(6, [False, True, True, True, True, True, True]))

# капиталистическая версия: собираем налоги ДАЖЕ с бедного кузнечика.
def getMinSumToCell(N, price):
	known_prices = [0, price[1], price[1] + price[2]]
	for ind in range(3, N + 1):
		print(price[ind], ind)
		known_prices.append(price[ind] + min([known_prices[ind - 1], known_prices[ind - 2]]))
	print(known_prices)
	return known_prices[N]

print(getMinSumToCell(6, [1, 1000, 6, 100, 200, 23, 12]))

# траектория + мин. стоимость с нуля. К херам снёс нулевую клетку.
def getMostCheapPath(cell, allow, price):
	cell_jumps = [1, 1]
	cell_prices = [price[0], price[0] + price[1]]
	cheap_path = []
	for ind in range(2, cell):
		if allow[ind]:
			price_cheapest_cell = min([cell_prices[ind - 1], cell_prices[ind - 2]])
			cheapest_cell = cell_prices.index(price_cheapest_cell)
			if cheapest_cell not in cheap_path:
				cheap_path.append(cheapest_cell)
			cell_prices.append(price[ind] + price_cheapest_cell)
	return (cell_prices[cell - 1], cheap_path)

print(getMostCheapPath(6, [False, True, True, True, True, True], [1, 1000, 6, 100, 200, 23]))