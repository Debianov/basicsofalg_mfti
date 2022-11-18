# рекурсивный Трибонначи. Хотел решить через него, но с первого раза не получилось.
def calculateTribonacciSequenece(tribonacciIndex, sum, n1, n2):
	if tribonacciIndex == 0:
		return sum
	else:
		return calculateTribonacciSequenece(tribonacciIndex - 1, sum + n1 + n2, sum, n1)
print(calculateTribonacciSequenece(15, 0, 0, 1))

# готовый вариант.
keepAlive = True
given = int(input())
tribonacci = [0, 0, 1]
N = 0

def calculateTribonacciSequence(lastN, N):
	diapason = (lastN, N - 2) if lastN == 0 else (lastN - 2, N - 2)
	for ind in range(*diapason):
		tribonacci.append(tribonacci[ind] + tribonacci[ind + 1] + tribonacci[ind + 2])

def tribonacciCheck():
	global keepAlive
	for element in tribonacci:
		if element > given:
			keepAlive = False
			print(tribonacci.index(element))
			break

while keepAlive:
	lastN = N
	N += 10
	calculateTribonacciSequence(lastN, N)
	tribonacciCheck()