	# TODO здесь, скорее всего, тоже нужно сделать методом обратного прохода формирование consecutive (lecture 11/practice/exercise 4.py, 1 вариант).
def lcs(A, B):
	matrix_counters = [[0] * (len(B) + 1) for _ in range((len(A) + 1))]
	consecutive = []
	for i in range(1, len(A) + 1):
		for j in range(1, len(B) + 1):
			if A[i - 1] == B[j - 1]:
				if not A[i - 1] in consecutive:
					consecutive.append(A[i - 1])
				else:
					if consecutive.count(A[i - 1]) < A.count(A[i - 1]):
						consecutive.append(A[i - 1])
				matrix_counters[i][j] = 1 + matrix_counters[i - 1][j - 1]
			else:
				matrix_counters[i][j] = max(matrix_counters[i - 1][j], matrix_counters[i][j - 1])
	return (consecutive, matrix_counters[-1][-1])

print(lcs([1, 1, 2, 5, 17], [1, 1, 2, 5, 12, 17]))