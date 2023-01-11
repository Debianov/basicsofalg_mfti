def calculate_min_cost(n, price):
	one_cell_price = [price[0], price[0] + price[1], price[0] + price[1] + price[2]] * (n - 3)
	for n in range(3, n):
		price_cheapest_cell = min(one_cell_price[n - 1], one_cell_price[n - 2], one_cell_price[n - 3])
		one_cell_price[n] = price_cheapest_cell + price[n]
	return one_cell_price[-1]

print(calculate_min_cost(6, [134, 234, 43, 5, 2, 2]))