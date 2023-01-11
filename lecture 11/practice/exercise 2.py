def estimate_count_jumps(n):
	jumps = [0] * n
	jumps[0] = 0 # 1 клетка
	jumps[1] = 1 # 2 клетка
	for n in range(2, n):
		jumps[n] = jumps[n - 1] + jumps[n - 2]
		jumps[n] += jumps[n // 3 - 1] if n % 3 == 0 else 0
	return jumps[n]

print(estimate_count_jumps(15))