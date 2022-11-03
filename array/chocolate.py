	#! хорошее объяснение: https://python.su/forum/post/216573/.
	# TODO переосмысление и домысление.

count = [0] * 100
n = int(input())
count[0] = 1
for ind in range(2, n + 1, 2):
	count[ind] += count[ind - 2]
	for innerInd in range(ind - 2, -1, -2):
		count[ind] += count[innerInd] * 2
print(count[n])