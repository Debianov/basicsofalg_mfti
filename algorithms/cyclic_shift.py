targetList = [1, 2, 3, 4, 5, 6, 234234, 1223123, 435534453]
listLength = len(targetList)
temp = targetList[0]
for ind in range(listLength - 1):
	targetList[ind] = targetList[ind + 1]
targetList[listLength - 1] = temp
print(targetList)

targetList = [2, 3, 4, 5, 6, 7]
listLength = len(targetList)
temp = targetList[listLength - 1]
for ind in range(listLength - 2, -1, -1):
	targetList[ind + 1] = targetList[ind]
targetList[0] = temp
print(targetList)