import stack

enter = input()

def bracket_check(enter):
	for symbol in enter:
		if symbol in "([":
			stack.push(symbol)
		elif symbol in ")]":
			if stack.isEmpty(): #"[])"
				return False
			left = stack.pop()
			if left == "(":
				right = ")"
			else:
				right = "]"
			if symbol != right:
				return False
		else:
			continue
	return stack.isEmpty() #"[]()("

print(bracket_check(enter))