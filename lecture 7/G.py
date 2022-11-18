countCollection = [0] * 100
arrayLength = int(input())
for _ in range(arrayLength):
	countCollection[int(input())] += 1
print(countCollection.index(max(countCollection)))