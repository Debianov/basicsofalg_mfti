number = -1
maximum = 0
while number != 0:
	number = int(input())
	if number == maximum:
		duplicateCount += 1
	elif number > maximum:
		maximum = number
		duplicateCount = 1
print(duplicateCount)