a = [1, 2, 3, 0, 4]

def lis(target):
	counters = [0] * (len(target) + 1)
	result_consecutive = []
	for i in range(1, len(target) + 1):
		a_max = 0
		for j in range(0, i):
			if target[i - 1] > target[j - 1] and counters[j] > a_max:
				a_max = counters[j]
		counters[i] = a_max + 1
	a_min = 0
	for i in range(1, len(counters)):
		if counters[i] > a_min:
			a_min = counters[i]
			result_consecutive.append(target[i - 1])
	return (max(counters), result_consecutive)

print(lis(a))