N = 100
sieve = [True] * N
primeNumbersList = []
sieve[0] = sieve[1] = False
for number in range(2, N):
	if sieve[number]:
		for innerNumber in range(number * 2, N, number):
			sieve[innerNumber] = False
		primeNumbersList.append(number)
print(primeNumbersList, sieve)