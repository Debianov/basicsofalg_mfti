# 1 вариант
def generate_permutations(M, prefix=""):
	if M == 0:
		print(prefix)
		return
	generate_permutations(M - 1, prefix + "1")
	generate_permutations(M - 1, prefix + "0")

# 2 вариант
def generate_permutations(N, M, prefix=None):
	prefix = prefix or []
	if M == 0:
		print(prefix)
		return
	for digit in range(1, N + 1):
		# if digit in prefix:
		# 	continue
		prefix.append(digit)
		generate_permutations(N, M - 1, prefix)
		prefix.pop()

generate_permutations(5, 5)