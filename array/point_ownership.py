enter = list(map(int, input().split(chr(32))))
pointX = enter[0]
pointY = enter[1]
circleRadius = enter[2]
if ((pointX) ** 2 + (pointY) ** 2 <= circleRadius ** 2):
	print("YES")
else:
	print("NO")