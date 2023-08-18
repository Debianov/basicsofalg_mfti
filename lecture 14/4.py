from operator import add, mul, sub, truediv

postfix_notation = "3 4 + 2 1 - * 5 /"

operators = {"+": add, "-": sub, "*": mul, "/": truediv}

def calculateByPostfixNotation(notation):
	split_expression = postfix_notation.split()
	operands_stack = []
	for token in split_expression:
		if token in operators:
			operator = token
			operator_func = operators[operator]
			operands_stack.append(operator_func(int(operands_stack.pop(-2)), int(operands_stack.pop(-1))))
		else:
			operand = token
			operands_stack.append(operand)
	return operands_stack[0]

try:
	print(calculateByPostfixNotation(postfix_notation))
except Exception:
	print("Выражение составлено не корректно.")