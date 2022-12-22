N = int(input())
students = []
for _ in range(N):
	enter = input().split()
	for (ind, format_pattern) in ((0, ".2f"), (1, ".3f")):
		enter[ind] = format(float(enter[ind]), format_pattern)
		students.append(enter[ind])
	print(students)
students.sort(key=lambda enter: (float(enter[1]), -float(enter[0])))
for student_indicators in students:
	print(" ".join(student_indicators))