def hoare_sort(enter):
	if len(enter) <= 1:
		return
	left = []
	middle = []
	right = []
	barrier_element = enter[0]
	for element in enter:
		if element < barrier_element:
			left.append(element)
		elif element == barrier_element:
			middle.append(element)
		else:
			right.append(element)
	hoare_sort(left)
	hoare_sort(right)
	for (index, element) in enumerate(left + middle + right):
		enter[index] = element
	print(left + middle + right, '****', enter, end='\n')
	# enter = (left + middle + right)[:]
	
enter = [32, 12, -53, 12, 32, -54, 14, 23, 90]
hoare_sort(enter)
print(enter)