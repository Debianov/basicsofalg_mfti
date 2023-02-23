import stack # абстракция

def processPolishNotation(enters):
	for enter in enters:
		if isinstance(enter, int):
			stack.push(enter)
		else:
			ACTIONS = "+-*/"
			if enter in ACTIONS:
				y = stack.pop()
				x = stack.pop()
				match ACTIONS.index(enter):
					case 0:
						stack.push(x + y)
					case 1:
						stack.push(x - y)
					case 2:
						stack.push(x * y)
					case 3:
						stack.push(x / y)
	if stack.size() == 1:
		return stack.pop()
	else:
		raise AssertionError("шоколадные конфетки")
		
print(processPolishNotation([5, 2, 7, "+", "*"]))