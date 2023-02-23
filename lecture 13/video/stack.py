"""
>>> clear()
>>> isEmpty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> isEmpty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> isEmpty()
True
"""

_stack = []

def push(x):
	"""
	>>> size = len(_stack)
	>>> push(5)
	>>> len(_stack)
	1
	>>> _stack[-1]
	5
	"""
	_stack.append(x)

def pop():
	return _stack.pop()

def top():
	return _stack[-1]

def clear():
	_stack.clear()

def size():
	return len(_stack)

def isEmpty():
	return size() == 0

if __name__ == "__main__":
	import doctest
	doctest.testmod()