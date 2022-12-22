enter = input()

last_symbol = ""
right_brackets_count = 0
left_brackets_count = 0
inner_mode = False
level = {}
result = "NO"
if enter.count(")") == enter.count("("):
	for symbol in enter:
		if symbol == "(":
			right_brackets_count += 1
			last_symbol = symbol
			level[right_brackets_count] = True
		elif symbol == ")":
			left_brackets_count += 1
			if level.get(left_brackets_count):
				result = "YES"
			else:
				result = "NO"
				break
else:
	result = "NO"
print(result)