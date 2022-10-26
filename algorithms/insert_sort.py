target = [3, 1, 2, 4]
for currentElementIndex in range(1, len(target)):
	for shiftedElementIndex in range(currentElementIndex, 0, -1):
		if target[shiftedElementIndex] < target[shiftedElementIndex - 1]:
			target[shiftedElementIndex], target[shiftedElementIndex - 1] = target[shiftedElementIndex - 1], target[shiftedElementIndex]
		else:
			break
	print(target)