#%%
import util
import matplotlib
import random
import math

def bubble_sort(a):
	for ind in range(0, len(a)):
		for innerInd in range(1, len(a) - ind):
			if a[innerInd] <= a[innerInd - 1]:
				a[innerInd], a[innerInd - 1] = a[innerInd - 1], a[innerInd]
if __name__ == "__main__":
	a = [5, 4, 3, 2, 1]
	bubble_sort(a)
	assert util.is_sorted(a)

permutation_flag = False
def bubble_sort_adaptive(a):
	global permutation_flag
	for ind in range(0, len(a)):
		if not permutation_flag and ind != 0:
			return
		for innerInd in range(1, len(a) - ind):
			if a[innerInd] <= a[innerInd - 1]:
				a[innerInd], a[innerInd - 1] = a[innerInd - 1], a[innerInd]
				permutation_flag = True
if __name__ == "__main__":
	a = [5, 4, 3, 2, 1]
	bubble_sort_adaptive(a)
	assert util.is_sorted(a)