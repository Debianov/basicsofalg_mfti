number = -1
origNumbers = []
duplicateNumbers = {}
while number != 0:
	number = int(input())
	if number in origNumbers:
		duplicateElement = duplicateNumbers.get(number)
		duplicateNumbers[number] = duplicateElement + 1 if duplicateElement else 2
	else:
		origNumbers.append(number)
print(duplicateNumbers.get(max(duplicateNumbers)))