# первый вариант: более красивый (ИМХО), но не проходит большой тест хз почему. К тому же, append юзать, вроде как, нельзя.
studentsNumber = int(input())
studentsResults = []
studentsSum = [0] * studentsNumber
while True:
	enter = input()
	if enter == "#":
		break
	else:
		(studentID, studentResult) = list(map(int, enter.split(chr(32))))
		studentsResults.append((studentID, studentResult))
		studentsSum[studentID] += studentResult
studentsResults.sort(key=lambda resultTuple: resultTuple[1], reverse=True)
studentsResults.sort(key=lambda resultTuple: studentsSum[resultTuple[0]], reverse=True)
print(" ".join(list(map(lambda resultTuple: str(resultTuple[1]), studentsResults))))

# второй вариант: рабочий, но на последние два теста я хз, что там вообще нужно.
studentsNumber = int(input())
studentsResults = [[] for _ in range(studentsNumber)]
while True:
	enter = input()
	if enter == "#":
		for studentPoints in studentsResults:
			studentPoints.sort(reverse=True)
		studentsResults.sort(key=lambda resultList: sum(resultList), reverse=True)   
		for studentPoints in studentsResults:
			for point in studentPoints:
				print(point, end=chr(32))
		break
	else:
		(studentID, studentPoints) = list(map(int, enter.split(chr(32))))
		studentsResults[studentID] += [studentPoints]