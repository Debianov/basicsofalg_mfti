N = int(input())
boardsRange = []
targetBoardsList = []

for _ in range(N):
	startRange = int(input()) # TODO
	endRange = int(input())
	colorRange = int(input())
	boardsRange.append((startRange, endRange, colorRange))

M = int(input())
for _ in range(M):
	targetBoardsList.append(int(input()))

changeResultColor = False
for boardNumber in targetBoardsList:
	for (startRange, endRange, color) in boardsRange:
		if int(startRange) <= int(boardNumber) <= int(endRange): #! лучше, чем проверять вхождение по range-y, поскольку памяти при последнем способе уходит дохера.
			changeResultColor = True
			resultColor = color
	print(resultColor if changeResultColor else 0, end=chr(32))
	changeResultColor = False
print()