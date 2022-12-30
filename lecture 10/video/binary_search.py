def left_binary_search(collection, target_element):
	left = -1
	right = len(collection)
	while right - left > 1:
		middle = (left + right) // 2
		if collection[middle] < target_element:
			left = middle
		else:
			right = middle
	return collection[middle]

collection = [1, 2, 3, 4, 5, 6, 7, 8]
print(left_binary_search(collection, 8)) 