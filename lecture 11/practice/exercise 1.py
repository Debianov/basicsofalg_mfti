def estimate_count_jumps(n):
	jumps = [0] * n
	jumps[0] = 0 # 1 клетка
	jumps[1] = 1 # 2 клетка
	jumps[2] = 2 # ...
	for n in range(3, n):
		jumps[n] = jumps[n - 1] + jumps[n - 2] + jumps[n - 3]
	return jumps[n]

print(estimate_count_jumps(6))