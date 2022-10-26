target = [2, 3, 6, 8, 1, 23423, -1]
for currentElementIndex in range(0, len(target) - 1):
	for shiftedElementIndex in range(currentElementIndex + 1, len(target)):
		if target[currentElementIndex] > target[shiftedElementIndex]:
			target[currentElementIndex], target[shiftedElementIndex] = target[shiftedElementIndex], target[currentElementIndex]
print(target)