from random import randint

N = 19

target = [randint(-10000, 10000) for i in range(N + 1)]

# 1 вариант: по методу из практической.
def calculate_min_cost(n, price):
	one_cell_price = [price[0], price[0] + price[1], price[0] + price[1] + price[2]] * (n - 3)
	min_cell_price = [0] * n
	path = []
	for n in range(3, n):
		near_cells = [one_cell_price[n - 1], one_cell_price[n - 2], one_cell_price[n - 3]]
		price_cheapest_cell = min(near_cells)
		cheapest_cell = [n - 1, n - 2, n - 3][near_cells.index(price_cheapest_cell)]
		min_cell_price[n] = cheapest_cell
		one_cell_price[n] = price_cheapest_cell + price[n]
	while n != 0:
		path.append(n + 1)
		next_point = n = min_cell_price[n]
	path.append(1)
	path.reverse()
	return (path, one_cell_price[-1])

print(calculate_min_cost(N, target))

# 2 вариант: свой вариант. В некоторых случаях добавляет лишние точки, если сравнивать с 1 вариантом.
def calculate_min_cost(n, price):
	one_cell_price = [price[0], price[0] + price[1], price[0] + price[1] + price[2]] * (n - 3)
	cheap_path = [1]
	for n in range(3, n):
		price_cheapest_cell = min(one_cell_price[n - 1], one_cell_price[n - 2], one_cell_price[n - 3])
		index_cheapest_cell = one_cell_price.index(price_cheapest_cell)
		one_cell_price[n] = price_cheapest_cell + price[n]
		if (index_cheapest_cell + 1) not in cheap_path:
			cheap_path.append(index_cheapest_cell + 1)
	cheap_path.append(n + 1)
	return (cheap_path, one_cell_price[-1])

print(calculate_min_cost(N, target))