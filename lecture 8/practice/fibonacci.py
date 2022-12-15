# 1 вариант из моей головы
startFibonacci = [0, 1]

def generateFibonacciUnit(n, deep=2, a=0, b=1):
	if n in startFibonacci:
		return startFibonacci[n]
	elif n == deep:
		return a + b
	return generateFibonacciUnit(n, deep + 1, b, a + b)

print(generateFibonacciUnit(7))

# 2 вариант: небольшое переосмысление интернетов. По скорости самый медленный вариант.
def generateFibonacciUnit(n):
	if n <= 1:
		return n
	return generateFibonacciUnit(n - 1) + generateFibonacciUnit(n - 2)

print(generateFibonacciUnit(7))

# 3 вариант: переосмысление интернетов
res = []
def updateFibonacciSequence(n, a=0, b=1, prefix=[0, 1]):
	if n == 0:
		return prefix
	sum = a + b
	prefix.append(sum)
	return updateFibonacciSequence(n - 1, b, sum)

print(updateFibonacciSequence(6))