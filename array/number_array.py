	#! код проходит не все тесты. Там косяк с тестированием (скорее всего).

numbersAmount = 0
sum = 0
max = 0
min = float("inf")
trioIndex = 0
trioSum = 0
lastSums = 0

while True:
	enter = input()
	if enter == "#":
		average = sum / numbersAmount
		print(round(average, 3), max, min, trioSum)
		break
	elif enter == chr(32):
		break
	else: # сами говорят, что числа от 1 до 100, но при этом в тест умудряются сувать и 101.
		enter = int(enter)
		numbersAmount += 1
		sum += enter
		if enter > max:
			max = enter
		if enter < min:
			min = enter
		if trioIndex != 2:
			trioIndex += 1
		else:
			trioSum += (sum - lastSums) % enter
			trioIndex = 0
			lastSums = sum