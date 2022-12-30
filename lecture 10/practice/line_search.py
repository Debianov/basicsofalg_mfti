def search(a, x):
	for elem in a:
		if elem == x:
			return a.index(x)

if __name__ == "__main__":
	assert search([1, 2, 3, 4, 5], 5) == 4
	assert search([1, 2, 3, 4, 5], 3) == 2