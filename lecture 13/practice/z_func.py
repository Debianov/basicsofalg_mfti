"""
Упражнение №1: Z-функция
Напишите Z-функцию. Пусть заголовком ее будет def z_func(s, n):
"""
# # неэффективная реализация.
# def z_func(s, n):
# 	z = [0] * n
# 	for i in range(1, n):
# 		z[i] = 0
# 		while i + z[i] < n and s[z[i]] == s[i + z[i]]:
# 			z[i] += 1
# 	return z

# print(z_func("abacaba", 7))

# эффективная реализация, не робит. 1 вариант
# def z_func(s, n):
# 	z = [0] * n
# 	l = 0
# 	r = 0
# 	for i in range(1, n):
# 		print("Цикл", i, l, r)
# 		if i <= r:
# 			print(z[i - l], r - i + 1)
# 			z[i] = min(z[i - l], r - i + 1)
# 		while i + z[i] < n and s[z[i]] == s[i + z[i]]:
# 			print(z[i])
# 			z[i] += 1
# 		if i + z[i] - 1 > r: # помечаем границы. z[i] используется, дабы учитывать весь совпадающий суффикс. 
# 			print(i + z[i] - 1)
# 			l = i
# 			r = i + z[i] - 1
# 	return z

# print(z_func("abababacababad", 14))

# z-func. 2 вариант. аналогично не робит.
# https://youtu.be/BP9LXwosFco
# def z_func(s, n):
# 	z = [0] * n
# 	l, r = 0, 1 # граница, в пределах которых уже происходили вычисления функции.
# 	for i in range(1, n - 1):
# 		shifted_i = i + z[i - l]
# 		if shifted_i < r: # входит в границу.
# 			z[i] = z[i - l] # может взять ранее вычисленные значения у похожих фрагментов.
# 		elif shifted_i == r: # входит в границу, но впритык.
# 			z[i] = r - i # берём всю границу
# 			while s[z[i]] == s[z[i] + i]: # + приращение для создания новой границы.
# 				z[i] += 1
# 			l = i
# 			r = i + z[i]
# 		else: # выходит за границу.
# 			z[i] = r - i # берём только границу, ранее вычисленную.
# 	return z

# не работает.
# def z_func(s, n):
# 	z = [0] * n
# 	l, r = 0, 0
# 	for i in range(1, n - 1):
# 		if i + z[i - l] < r:
# 			z[i] = z[i - l]
# 		elif i + z[i - l] > r:
# 			z[i] = i - r
# 		elif i + z[i - l] == r:
# 			z[i] = i - r
# 			while s[i + z[i]] == s[z[i]]:
# 				z[i] += 1
# 			l = i
# 			r = i + z[i]
# 	return z

# опять не работает
# def z_func(s, n):
# 	z = [0] * n
# 	l, r = 0, 0
# 	for i in range(1, n - 1):
# 		z[i] = min(z[i - l], r - i)
# 		while s[i + z[i]] == s[z[i]]:
# 			z[i] += 1
# 		if i + z[i] > r:
# 			l = i
# 			r = i + z[i]
# 	return z

# print(z_func("abcdefghi", 9))

# z-функция: рабочие варианты (https://youtu.be/2trqpOFhqEc)
# https://codeforces.com/edu/course/2/lesson/3/3
# 1 вариант.
def z_func(s, n):
	z = [0] * n
	l = r = left = right = 0
	for i in range(1, n):
		if i <= r:
			if z[i - l] < r - i:
				z[i] = z[i - l]
			else:
				z[i] = r - i
				while i + z[i] < n and s[z[i]] == s[i + z[i]]:
					z[i] += 1
		else:
			while i + z[i] < n and s[z[i]] == s[i + z[i]]:
				z[i] += 1
		if r <= i + z[i]:
			l = i
			r = i + z[i]
	return z

# 2 вариант: сокращённый.
def z_func(s, n):
	z = [0] * n
	l = r = 0
	for i in range(1, n):
		if i <= r:
			z[i] = min(z[i - l], r - i) # z[i - l] в случае, если z[i] не выходит за границы. В противном случае
			# берём известный нам остаток r - i, не выходящий за r, а дальше наивный алгоритм.
		while i + z[i] < n and s[z[i]] == s[i + z[i]]: # наивный алгоритм.
			z[i] += 1
		if r < i + z[i]: # если наш новоиспечённый совпадающий суффикс выходит за пределы r, мы делаем с границами
			# жах-жах.
			l = i
			r = i + z[i]
	return z

"""
Упражнение №2: Поиск подстроки
Пусть даны две строки. Найти все вхождения второй строки в первую.
"""
def z_func(string, substring, n):
	s = substring + "#" + string
	n += 1
	z = [0] * n
	l = r = 0
	for i in range(1, n):
		if i <= r:
			z[i] = min(z[i - l], r - i) # z[i - l] в случае, если z[i] не выходит за границы. В противном случае
			# берём известный нам остаток r - i, не выходящий за r, а дальше наивный алгоритм.
		while i + z[i] < n and s[z[i]] == s[i + z[i]]: # наивный алгоритм.
			z[i] += 1
		if r < i + z[i]: # если наш новоиспечённый совпадающий суффикс выходит за пределы r, мы делаем с границами
			# жах-жах.
			l = i
			r = i + z[i]
	# sub_len = len(substring) # мой вариант
	# for i in range(len(substring), n):
	# 	print(z[i], z, i)
	# 	if z[i] % sub_len == 0:
	# 		print(i)
	# 		print("Зарегистрировано вхождение: [{}:{}]".format(i, i + z[i]))
	for i in range(1, n): # правильный вариант. Перед этим нужно разделитель сделать между string и substring.
		if z[i] == len(substring):
			print("Вхождение!!!!", i)
	return (z, s)

"""
Упражнение №3: Количество разных подстрок
Найти число всех различных подстрок входящих в данную.
"""
#! не уверен, что правильно.
def z_func(s, n):
	z = [0] * n
	l = r = 0
	for i in range(1, n):
		if i <= r:
			z[i] = min(z[i - l], r - i) # z[i - l] в случае, если z[i] не выходит за границы. В противном случае
			# берём известный нам остаток r - i, не выходящий за r, а дальше наивный алгоритм.
		while i + z[i] < n and s[z[i]] == s[i + z[i]]: # наивный алгоритм.
			z[i] += 1
		if r < i + z[i]: # если наш новоиспечённый совпадающий суффикс выходит за пределы r, мы делаем с границами
			# жах-жах.
			l = i
			r = i + z[i]
	return z

def substrings_search(s, n):
	current_s = s[0]
	# k = 0 #? смысл от добавлений символов каждый раз? (http://judge.mipt.ru/mipt_cs_on_python3/labs/lab13.html#o8)
	# for symbol_index_for_concatenate in range(1, n):
	# 	current_s += s[symbol_index_for_concatenate]
	# 	current_s_length = len(current_s)
	# 	z = z_func(current_s[::-1], current_s_length)
	# 	print("При", symbol_index_for_concatenate, current_s, "z_func=", z)
	# 	z_max = max(z)
	# 	print('а z_max=', z_max)
	# 	k = current_s_length - z_max
	# 	print(k)
	# return k
	z = z_func(s[::-1], n) # TODO до меня не очень дошла суть данного механизма + я не все выведенные подстроки нашёл.
	current_s_length = len(s)
	z_max = max(z)
	k = current_s_length - z_max
	return k

"""
Упражнение №4: Период строки
Для данной строки s найти строку p минимальной длины, такую что s можно представить как конкатенацию одной или нескольких копий p.
"""
# # 2 вариант: сокращённый.
def z_func(string, n):
	z = [0] * n
	l = r = left = right = 0
	for i in range(1, n):
		if i <= r:
			z[i] = min(z[i - l], r - i)
		while i + z[i] < n and string[z[i]] == string[i + z[i]]:
			z[i] += 1
		if r < i + z[i]:
			l = i
			r = i + z[i]
	period = ""
	# for i in range(1, n): # мой вариант
	# 	if z[i] == n - i:
	# 		period = string[0:n - z[i]]
	# 		break
	for i in range(1, n):
		print(i, z[i], n)
		if i + z[i] == n and n % i == 0: # вариант куда более годный.
			print("неск раз?")
			period = string[0:n - z[i]]
	return (z, string, period)