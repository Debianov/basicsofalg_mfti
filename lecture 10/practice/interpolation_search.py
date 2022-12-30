	# TODO если не будем упоминать на лекциях — записать с нуля.
def interpolation_search(lis, key):
	low = 0
	high = len(lis) - 1
	while low < high:
		mid = low + int((high - low) * (key - lis[low])/(lis[high] - lis[low]))
		if key < lis[mid]:
			high = mid - 1
		elif key > lis[mid]:
			low = mid + 1
		else:
			return mid

# assert interpolation_search([1, 2, 3, 4, 5], 5) == 4
# assert interpolation_search([1, 2, 3, 4, 5], 3) == 2
# assert interpolation_search([1, 2, 3, 4, 5], 1) == 0