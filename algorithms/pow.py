def power(x, n):
	if n == 0:
		return 1
	elif n % 2 == 0:
		return power (x ** 2, n // 2)
	else:
		return power(x, n - 1) * x

print(power(-7, 3))