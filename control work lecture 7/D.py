max = -float("inf")
amountNumber = 0
while True:
	enter = int(input())
	if enter == 0:
		break
	elif enter % 2 == 0 and max < enter:
		max = enter
print(max if not max == -float("inf") else 0)