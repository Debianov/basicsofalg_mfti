# 1 вариант: скопирован с урока.
def check_sort(A, ascending=False):
	flag = True
	s = 2 * int(ascending) - 1
	for i in range(0, len(A) - 1):
		if s * A[i] > s * A[i + 1]:
			flag = False
			break
	return flag

print(check_sort([5, 3, 2], ascending=False))

# 2 вариант: сам.
def check_sort(target, ascending=True):
	flag = True
	funcs = [check_descending, check_ascending]
	for ind in range(0, len(target) - 1):
		flag = funcs[ascending](target[ind], target[ind + 1])
		if flag is False:
			break
	return flag

def check_ascending(left_number, right_number):
	return True if left_number < right_number else False

def check_descending(left_number, right_number):
	return True if left_number > right_number else False

print(check_sort([5, -10, 3, 2], ascending=False))

# 3 вариант: на базе 1 варианта.
def check_sort(sequence, ascending=True):
	flag = True
	factor = 2 * ascending - 1
	for ind in range(0, len(sequence) - 1):
		if factor * sequence[ind] > factor * sequence[ind + 1]:
			flag = False
			break
	return flag

print(check_sort([2, -100, 3, 5], ascending=True))