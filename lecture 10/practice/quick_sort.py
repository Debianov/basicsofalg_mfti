#%%
import util
import matplotlib
import random
import math

def quick_sort_first(a):
	if len(a) <= 1:
		return
	barrier_element = a[0]
	left = []
	middle = []
	right = []
	for element in a:
		if barrier_element > element:
			left.append(element)
		elif barrier_element == element:
			middle.append(element)
		else:
			right.append(element)
	quick_sort_first(left)
	quick_sort_first(right)
	for (ind, element) in enumerate(left + middle + right):
		a[ind] = element
a = [5, 4, 3, 2, 1]
quick_sort_first(a)
assert util.is_sorted(a)

def quick_sort_middle(a):
	if len(a) <= 1:
		return
	a_middle = len(a) // 2
	barrier_element = a[a_middle]
	left = []
	middle = []
	right = []
	for element in a:
		if barrier_element > element:
			left.append(element)
		elif barrier_element == element:
			middle.append(element)
		else:
			right.append(element)
	quick_sort_middle(left)
	quick_sort_middle(right)
	for (ind, element) in enumerate(left + middle + right):
		a[ind] = element
a = [5, 4, 3, 2, 1]
quick_sort_middle(a)
assert util.is_sorted(a)

def quick_sort_random(a):
	if len(a) <= 1:
		return
	barrier_element = random.choice(a)
	left = []
	middle = []
	right = []
	for element in a:
		if barrier_element > element:
			left.append(element)
		elif barrier_element == element:
			middle.append(element)
		else:
			right.append(element)
	quick_sort_random(left)
	quick_sort_random(right)
	for (ind, element) in enumerate(left + middle + right):
		a[ind] = element
a = [5, 4, 3, 2, 1]
quick_sort_random(a)
assert util.is_sorted(a)

if __name__ == "__main__":
	util.plot_quick_sort_results(
		('Первый элемент в качестве опорного', quick_sort_first),
		('Средний элемент в качестве опорного', quick_sort_middle),
		('Произвольный элемент в качестве опорного', quick_sort_random)
	)