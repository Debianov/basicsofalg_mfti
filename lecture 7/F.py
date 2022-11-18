def calculateEuclid(a, b):
	return a if b == 0 else calculateEuclid(b, a % b)
print(calculateEuclid(int(input()), int(input())))