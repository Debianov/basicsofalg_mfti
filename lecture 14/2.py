check_string = input()
left_brackets = []
for symbol in check_string:
	if (left_bracket := symbol) in ["(", "{", "/"]:
		left_brackets.append(left_bracket)
	if (right_bracket := symbol) in [")", "}", "/"]:
		if left_brackets:
			raise Exception("Скобочная запись не верна.")
		left_bracket = left_brackets.pop()
		match right_bracket:
			case ")":
				check_result = left_bracket == "("
			case "}":
				check_result = left_bracket == "{"
			case "\\":
				check_result = left_bracket == "/"
		if not check_result:
			raise Exception("Скобочная запись не верна.")
else:
	if left_brackets:
		raise Exception("Скобочная запись не верна.")
