# # по пути наименьшего сопротивления.
enter = input()
enter = enter[:enter.find(".") + 1]
def ordSort(enter):
	if not enter == '.':
		return ord(enter)
	return float("inf")
print("".join(sorted(enter, key=ordSort)))

# по пути наибольшего сопротивления.
enter = input()
enter = enter[:enter.find(".")]
text_line = []

for symbol in enter:
	text_line.append(symbol)

def separate(enter):
	if len(enter) <= 1:
		return
	end = len(enter)
	middle = end // 2
	left = enter[0:middle]
	right = enter[middle:end]
	separate(left)
	separate(right)
	merge_result = merge(left, right)
	for ind in range(0, len(merge_result)):
		enter[ind] = merge_result[ind]

def merge(left, right):
	left_cursor = right_cursor = main_cursor = 0
	main = [""] * (len(left) + len(right))
	while left_cursor < len(left) and right_cursor < len(right):
		if ord(left[left_cursor]) <= ord(right[right_cursor]):
			main[main_cursor] = left[left_cursor]
			left_cursor += 1
		else:
			main[main_cursor] = right[right_cursor]
			right_cursor += 1
		main_cursor += 1
	while left_cursor < len(left):
		main[main_cursor] = left[left_cursor]
		left_cursor += 1
		main_cursor += 1
	while right_cursor < len(right):
		main[main_cursor] = right[right_cursor]
		right_cursor += 1
		main_cursor += 1
	return main

separate(text_line)
print("".join(text_line) + ".")