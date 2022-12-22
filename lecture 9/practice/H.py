n = int(input())
numbers = (input()).split(' ')
for p1 in range(n - 1):
	for p2 in range(p1 + 1, n):
		if numbers[p1][::-1] > numbers[p2][::-1]:
			numbers[p1], numbers[p2] = numbers[p2], numbers[p1]
for sort_number in numbers:
	print(sort_number, end=' ')
print()