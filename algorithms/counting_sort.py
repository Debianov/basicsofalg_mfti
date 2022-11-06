target = [3, 2, 9, 0, 0, 0, 0, 0, 4, 4, 4, 2, 3, 3, 5, 5]
countsCollection = {key:0 for key in range(0, 10)}
for number in target:
	if number in range(0, 10):
		countsCollection[number] += 1
for (number, count) in countsCollection.items():
	if count != 0:
		numberAsStr = str(number)
		result = (numberAsStr + chr(32)) * (count - 1)
		result += numberAsStr
		print(result, end=' ')
print()