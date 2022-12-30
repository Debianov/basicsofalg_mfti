def fib(N):
	fib_row = [0, 1]
	for ind in range(2, N):
		fib_row.append(fib_row[ind - 1] + fib_row[ind - 2])
	return fib_row[N - 1]

print(fib(6))