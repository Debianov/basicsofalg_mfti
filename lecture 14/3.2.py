operators_priority = {"+": 1, "-": 1, "/": 2, "*": 2, "(": float("inf"), ")": float("inf")}

def convertInfixToPostfix(infix_notation):
	postfix_notation = ''
	stack = []
	for symbol in infix_notation:
		if symbol == "(":
			stack.append(symbol)
		elif symbol == ")":
			while stack[-1] != "(":
				postfix_notation += stack.pop()
			stack.pop()
		elif symbol in list(operators := operators_priority.keys()):
			operator = symbol
			while stack and operators_priority[stack[-1]] <= operators_priority[operator]:
				postfix_notation += stack.pop()
			stack.append(operator)
		else:
			operand = symbol
			postfix_notation += symbol
	while stack:
		postfix_notation += stack.pop()
	return postfix_notation

print(convertInfixToPostfix('(2-3)*(12-10)+4/2'))