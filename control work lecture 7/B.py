# 	#! выводит в одном тесте ошибку, хотя там треугольника не существует (стороны: 6 6 12).
# enter = []
# for sideNumber in range(3):
# 	enter.append(int(input()))
# 	tmp = enter[0]
# for ind in range(3):
# 	for innerInd in range(1, len(enter) - ind): # или enter.sort(). Но я не ищу лёгких путей.
# 		if enter[innerInd] < enter[innerInd - 1]:
# 			enter[innerInd], enter[innerInd - 1] = enter[innerInd - 1], enter[innerInd]
# a, b, c = enter
# trianglePossibility = (a <= b + c and b <= a + c and c <= a + b)
# if a <= b + c and b <= a + c and c <= a + b:
# 	if c**2 == a**2 + b**2:
# 		print("right")
# 	elif c**2 < a**2 + b**2:
# 		print("acute")
# 	elif c**2 > a**2 + b**2:
# 		print("obtuse")
# else:
# 	print("impossible")

# # интересный вариант из инета (не допилен)
# if a + b <= c:
#    print('impossible')
# else:
#    t = a * a + b * b - c * c #? а как.
#    print(('right', 'obtuse', 'acute')[(t < 0) - (t > 0)]) #? а как.
# print([(t < 0) - (t > 0)])
# print(True - True)