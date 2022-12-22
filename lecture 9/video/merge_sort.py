
target = [5, 2, 7, 3, 1]

def separate(enter):
	if len(enter) <= 1:
		return
	middle = len(enter) // 2
	L = enter[0:middle]
	R = enter[middle:len(enter)]
	separate(L)
	separate(R)
	C = merge(L, R)
	for ind in range(len(C)):
		enter[ind] = C[ind]

def merge(L, R):
	leftCrs = rightCrs = centralCrs = 0
	C = [0] * (len(L) + len(R))
	while leftCrs < len(L) and rightCrs < len(R):
		if L[leftCrs] <= R[rightCrs]:
			C[centralCrs] = L[leftCrs]
			leftCrs += 1
		else:
			C[centralCrs] = R[rightCrs]
			rightCrs += 1
		centralCrs += 1
	while leftCrs < len(L):
		C[centralCrs] = L[leftCrs]
		leftCrs += 1
		centralCrs += 1
	while rightCrs < len(R):			
		C[centralCrs] = R[rightCrs]
		rightCrs += 1
		centralCrs += 1
	return C

separate(target)
print(target)