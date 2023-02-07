	# TODO про МФТИ таск дополнить. # TODO ответ на вывод поискать.
def levenstein(A, B):
	matrix = [[((i + j) if i * j == 0 else 0) for j in range(len(B) + 1)] for i in range(len(A) + 1)]
	symbols_to_change = []
	symbols_to_remove = []
	symbols_to_append = []
	for i in range(1, len(A) + 1):
		for j in range(1, len(B) + 1):
			if A[i - 1] == B[j - 1]:
				matrix[i][j] = matrix[i - 1][j - 1]
			else:
				matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) # поиск min также по диагонали matrix[i - 1][j - 1] обусловлена
				# тем, что может содержать минимальный count, если проверяется последний элемент A и B, причём у обоих этих объектов он не одинаков
				# (например: "boba" и "bobo").
	while i > 0 and j > 0:
		if A[i - 1] == B[j - 1]:
			i -= 1
			j -= 1
		else:
			if A[i - 1] not in symbols_to_change and j - 1 == i - 1:
				symbols_to_change.append(A[i - 1])
				symbols_to_append.append(B[j - 1])
				print("{} index {} --> {}".format(A[i - 1], i - 1, B[j - 1]))
			elif A[i - 1] not in symbols_to_change and ((i - 1 > j - 1) or (i - 1 < j - 1)):
				print("{} index {} --> --".format(A[i - 1], i - 1))
			else:
				print("{} + {}".format(symbols_to_append[-1], B[j - 1]))
				symbols_to_append.append(B[j - 1])
			forMinCheck = [matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]]
			minCount = min(forMinCheck)
			match forMinCheck.index(minCount):
				case 0:
					i -= 1
				case 1:
					j -= 1
				case 2:
					i -= 1
					j -= 1
	symbols_to_change = list(reversed(symbols_to_change))
	return matrix[len(A)][len(B)]

print(levenstein("boba", "bos"))