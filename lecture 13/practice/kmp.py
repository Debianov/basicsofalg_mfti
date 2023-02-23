"""
Упражнение №5: Префикс-функция
Напишите префикс-функцию. Пусть заголовком ее будет def p_func(s, n):
"""
# мне лень сигнатуру менять.
def getPrefixFunction(x):
	max_prefix_and_suffix_lengths = [0] * len(x)
	for i in range(1, len(x)):
		j = max_prefix_and_suffix_lengths[i - 1]
		while j > 0 and x[j] != x[i]:
			j = max_prefix_and_suffix_lengths[j - 1]
		if x[j] == x[i]:
			j += 1
		max_prefix_and_suffix_lengths[i] = j
	return max_prefix_and_suffix_lengths

"""
Упражнение №6: Поиск подстроки
Пусть даны две строки. Найти все вхождения второй строки в первую с помощью алгоритма Кнута-Морриса-Пратта.
"""
def getPrefixFunction(x):
	max_prefix_and_suffix_lengths = [0] * len(x)
	for i in range(1, len(x)):
		j = max_prefix_and_suffix_lengths[i - 1]
		while j > 0 and x[j] != x[i]:
			j = max_prefix_and_suffix_lengths[j - 1]
		if x[j] == x[i]:
			j += 1
		max_prefix_and_suffix_lengths[i] = j
	return max_prefix_and_suffix_lengths

def executeKMPAlgorithm(s, x):
	d = getPrefixFunction(x)
	i = j = 0
	result = []
	while i < len(s):
		if x[j] == s[i]:
			i += 1
			j += 1
		elif j == 0:
			i += 1
		else:
			j = d[j - 1]
		if j >= len(x):
			result.append(i - j)
			j = 0
	return result

"""
Упражнение №7: Поиск подстроки онлайн
В первой строке ввода — число n, количество букв в паттерне. Во второй строке —
паттерн, строка которую нужно искать в тексте. В каждой из последующих строк —
символы текста, по одному в каждой строке. Необходимо вывести позиции вхождений
паттерна в текст. Длина текста заранее не известна, он может быть очень большим.
"""
def getPrefixFunction(pattern, length):
	max_prefix_and_suffix_lengths = [0] * length
	for i in range(1, len(pattern)):
		j = max_prefix_and_suffix_lengths[i - 1]
		while j > 0 and pattern[j] != pattern[i]:
			j = max_prefix_and_suffix_lengths[j - 1]
		if pattern[j] == pattern[i]:
			j += 1
		max_prefix_and_suffix_lengths[i] = j
	return max_prefix_and_suffix_lengths

def executeOnlineKMPAlgorithm(pattern, pattern_length, prefix_suffix_lengths):
	d = getPrefixFunction(pattern, pattern_length)
	j = i = 0
	text = ""
	while True:
		if j >= len(pattern):
			print("Обнаружено совпадение, начиная с позиции", i - j)
			j = 0
		enter = input()
		if enter == " ":
			break
		text += enter
		if pattern[j] == text[i]:
			i += 1
			j += 1
		elif j == 0:
			i += 1
		else:
			j = d[j - 1]

# pattern_n = int(input())
# pattern = input()
# prefix_suffix_lengths = getPrefixFunction(pattern, pattern_n)

"""
Упражнение №8: Количество разных подстрок
Найти число всех различных подстрок входящих в данную с помощью префикс-функции.
"""
def executePrefixFunction(x):
	max_prefix_and_suffix_lengths = [0] * len(x)
	for i in range(1, len(x)):
		j = max_prefix_and_suffix_lengths[i - 1]
		while j > 0 and x[j] != x[i]:
			j = max_prefix_and_suffix_lengths[j - 1]
		if x[j] == x[i]:
			j += 1
		max_prefix_and_suffix_lengths[i] = j
	return max_prefix_and_suffix_lengths

def findSubstrings(s):
	max_prefix_and_suffix_lengths = executePrefixFunction(s)
	return len(s) - max(max_prefix_and_suffix_lengths)

"""
Упражнение №9: Период строки
Для данной строки s найти строку p минимальной длины, такую что s можно представить как конкатенацию одной или нескольких копий p.
Используйте префикс-функцию.
"""
def executePrefixFunction(x):
	max_prefix_and_suffix_lengths = [0] * len(x)
	for i in range(1, len(x)):
		j = max_prefix_and_suffix_lengths[i - 1]
		while j > 0 and x[j] != x[i]:
			j = max_prefix_and_suffix_lengths[j - 1]
		if x[j] == x[i]:
			j += 1
		max_prefix_and_suffix_lengths[i] = j
	return max_prefix_and_suffix_lengths

def findPeriod(s):
	max_prefix_and_suffix_lengths = executePrefixFunction(s)
	length_s = len(s)
	period = "blank"
	for i in range(1, length_s):
		if length_s % (length_s - max_prefix_and_suffix_lengths[i]) == 0:
			period = s[0:length_s - max_prefix_and_suffix_lengths[i]]
	return period