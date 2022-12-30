def binary_search(a, x):
	left_bound = 0
	right_bound = len(a)
	while True:
		middle = (left_bound + right_bound) // 2
		if a[middle] > x:
			right_bound = middle
		elif a[middle] == x:
			return a.index(x)
		else:
			left_bound = middle
	return a[middle]

if __name__ == "__main__":
	assert binary_search([1, 2, 3, 4, 5], 5) == 4
	assert binary_search([1, 2, 3, 4, 5], 3) == 2
	assert binary_search([1, 2, 3, 4, 5], 1) == 0