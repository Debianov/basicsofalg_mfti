enter = list(map(int, input().split(chr(32))))
if len(enter) == 3:
	x = resultDeposit = enter[0] # чисто как эквивалент букве из задачи.
	p = enter[1]
	y = enter[2]
else:
	x = resultDeposit = p = y = 0
currentYear = 0
while resultDeposit < y:
	resultDeposit += resultDeposit * (p / 100)
	resultDeposit = int(resultDeposit * 100) / 100 # избавляемся от дроби в части копеек.
	currentYear += 1
print(currentYear)