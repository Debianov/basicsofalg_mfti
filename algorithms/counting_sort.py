counts = [0] * 10 # ОДЗ: 0 - 9.

while True:
	number = int(input())
	if not number == -1:
		counts[number] += 1
	else:
		break

for (ind, count) in enumerate(counts):
	if count != 0:
		print((str(ind) + chr(32)) * count, end="")
print()