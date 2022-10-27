target = [3, 1, 2, 4]
for topLimit in range(1, len(target)):
	for comparedElementIndex in range(topLimit, 0, -1):
		if target[comparedElementIndex] < target[comparedElementIndex - 1]:
			target[comparedElementIndex], target[comparedElementIndex - 1] = target[comparedElementIndex - 1], target[comparedElementIndex]
		else:
			break
print(target)