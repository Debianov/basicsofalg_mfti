target = [2, 5, -1, 3, -5, 0]
for choiceElementIndex in range(0, len(target) - 1):
	for comparedElementIndex in range(choiceElementIndex + 1, len(target)):
		if target[comparedElementIndex] < target[choiceElementIndex]:
			target[comparedElementIndex], target[choiceElementIndex] = target[choiceElementIndex], target[comparedElementIndex]
print(target)