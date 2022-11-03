N = int(input())
maxInRow = 0
currentInRow = 0
for index in range(N):
	number = int(input())
	if number == 1:
		currentInRow += 1
	if number == 0 or index == N - 1:
		if currentInRow > maxInRow:
			maxInRow = currentInRow
		currentInRow = 0
print(maxInRow)