	# TODO башеньки в консоли.

# 1 вариант — неверный.
target = [1, 2, 3, 4, 5, 6]
result = []
def moveCircle(target, n):
	if n != 0:
		tmp = target[-n:n - 1]
		moveCircle(tmp, n - 1)
		result.append(target[-1]) 
moveCircle(target, len(target))
print(result)

# 2 вариант — верный.
source = [1, 2, 3, 4]
tmp = []
destination = []
stepCount = 0
def moveCircle(source, tmp, destination, n):
	global stepCount
	if n == 1:
		source.remove(1)
		destination.append(1)
		stepCount += 1
		print("Step {}: {}, {}, {}".format(stepCount, source, tmp, destination))
		return
	moveCircle(source, destination, tmp, n - 1)
	source.remove(n)
	destination.append(n)
	stepCount += 1
	print("Step {}: {}, {}, {}".format(stepCount, source, tmp, destination))
	moveCircle(tmp, source, destination, n - 1)
moveCircle(source, tmp, destination, 4)
print(destination)	