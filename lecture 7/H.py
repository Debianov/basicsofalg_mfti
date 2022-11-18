# 1 вариант: по проще.
def dot_product(n, vector1, vector2):
	result = list(zip(vector1, vector2))
	for (index, (coord1, coord2)) in enumerate(result):
		result.remove((coord1, coord2))
		result.insert(index, coord1 * coord2)
	return sum(result)

# 2 вариант: по сложнее.
def dot_product(n, vector1, vector2):
	sum = 0
	for ind in range(n):
		sum += vector1[ind] * vector2[ind]
	return sum