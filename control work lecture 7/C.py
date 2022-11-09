sum = 0
amountNumber = 0
while True:
	enter = int(input())
	if enter == 0:
		break
	else:
		sum += enter
		amountNumber += 1
print(round(sum / amountNumber, 2))