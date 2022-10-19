targetList = [1, 2, 3, 4, 5, 6, 234234, 1223123, 435534453]

for index in range(len(targetList) // 2):
	targetList[index], targetList[len(targetList) - 1 - index] = targetList[len(targetList) - 1 - index], targetList[index]
print(targetList)

for index in range(len(targetList) // 2, -1, -1):
	targetList[index], targetList[len(targetList) - 1 - index] = targetList[len(targetList) - 1 - index], targetList[index]
print(targetList)