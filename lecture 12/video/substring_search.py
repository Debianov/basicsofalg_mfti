A = "abacabad"
B = "abac"

def equal(A, B): # O(N)
	if len(A) != len(B):
		return False
	for i in range(len(A)):
		if A[i] != B[i]:
			return False
	return True

def findSubstring(target_string, substring): # O(M * N)
	for i in range(0, len(target_string) - len(substring)): #? и зочем?
		if equal(target_string[i:i + len(substring)], substring):
			print(i)

findSubstring(A, B)

def getPrefixFunction(x):
	max_prefix_and_suffix_lengths = [0] * len(x)
	for i in range(1, len(x)):
		j = max_prefix_and_suffix_lengths[i - 1]
		while j > 0 and x[j] != x[i]:
			j = max_prefix_and_suffix_lengths[j - 1]
		if x[j] == x[i]:
			j += 1
		max_prefix_and_suffix_lengths[i] = j
	return max_prefix_and_suffix_lengths

def executeKMPAlgorithm(s, x): # O(M * N)
	d = getPrefixFunction(x)
	i = j = 0
	while i < len(s) and j < len(x):
		if x[j] == s[i]:
			i += 1
			j += 1
		elif j == 0:
			i += 1
		else:
			j = d[j - 1]
	else:
		if j == len(x):
			return i - j
		return None

print(executeKMPAlgorithm("abcabeabcabcabd", "abcabd"))