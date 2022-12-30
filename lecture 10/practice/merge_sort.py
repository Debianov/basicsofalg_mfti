#%%
import util
import matplotlib
import random
import math

def merge_sort(a):
	if len(a) <= 1:
		return
	middle = len(a) // 2
	L = a[0:middle]
	R = a[middle:len(a)]
	merge_sort(L)
	merge_sort(R)
	result = merge(L, R)
	for (ind, element) in enumerate(result):
		a[ind] = result[ind]

def merge(L, R):
	left_cursor = right_cursor = 0
	result = []
	while left_cursor < len(L) and right_cursor < len(R):
		if L[left_cursor] < R[right_cursor]:
			result.append(L[left_cursor])
			left_cursor += 1
		else:
			result.append(R[right_cursor])
			right_cursor += 1
	while left_cursor < len(L):
		result.append(L[left_cursor])
		left_cursor += 1
	while right_cursor < len(R):
		result.append(R[right_cursor])
		right_cursor += 1
	return result

if __name__ == "__main__":
	a = [5, 4, 3, 2, 1]
	merge_sort(a)
	assert util.is_sorted(a)

#! не уверен, что это то, что требовалось в дополнительном задании, но он работает быстрее ^_^.
#! lecture 10/practice/Битва двух маржов.png
#! lecture 10/practice/Битва двух маржов 2.png
def alt_merge_sort(u_list, start=None, end=None):
	start = start if start else 0
	end = end if end else len(u_list)
	if end - start > 1:
		mid = (start + end) // 2
		alt_merge_sort(u_list, start, mid)
		alt_merge_sort(u_list, mid, end)
		alt_merge(u_list, start, mid, end)

def alt_merge(u_list, start, mid, end):
	left = u_list[start:mid]
	right = u_list[mid:end]
	main_cursor = start
	left_cursor = 0
	right_cursor = 0
	while start + left_cursor < mid and mid + right_cursor < end:
		if left[left_cursor] <= right[right_cursor]:
			u_list[main_cursor] = left[left_cursor]
			left_cursor += 1
		else:
			u_list[main_cursor] = right[right_cursor]
			right_cursor += 1
		main_cursor += 1
	while start + left_cursor < mid:
		u_list[main_cursor] = left[left_cursor]
		left_cursor += 1
		main_cursor += 1
	while mid + right_cursor < end:
		u_list[main_cursor] = right[right_cursor]
		right_cursor += 1
		main_cursor += 1

if __name__ == "__main__":
	a = [5, 4, 3, 2, 1]
	alt_merge_sort(a)
	assert util.is_sorted(a)
# %%
