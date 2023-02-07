def evaluateMinEnergyCounts(n, lengths):
	if n <= 1:
		return 0
	energyCounts = [0, abs(lengths[1] - lengths[0])]
	for jump in range(2, n):
		E1 = 3 * abs(lengths[jump] - lengths[jump - 2]) + energyCounts[jump - 2]
		E2 = abs(lengths[jump] - lengths[jump - 1]) + energyCounts[jump - 1]
		if E1 < E2:
			energyCounts.append(E1)
		else:
			energyCounts.append(E2)
	return energyCounts[-1]

n = int(input())
lengths = []
for _ in range(n):
	lengths.append(int(input()))

print(evaluateMinEnergyCounts(n, lengths))