# очень хотелось сделать через append и max, но пока ещё не надо, видимо. Если вы смотрели код до этого и думали, какой же я дурачёк, что не юзал такие
# очевидные методы и функции и делал всё вручную, то могу вам сказать, что тут нужно рассматривать контекст лекций, к которым приложены эти задания.

# 1 вариант: выдаёт MemoryError.
enterCollection = []
while True:
	enter = int(input())
	if enter != 0:
		enterCollection += [enter]
	else:
		break
max = enterCollection[0]
for number in enterCollection[1:-5]:
	if max < number:
		max = number
print(max)

# 2 вариант. Попытался в оптимизацию, но тест всё равно не прошёл :D. Без игнора built-in методов.
past5Numbers = []
current5Numbers = []
maxsCollection = []
result = 0
while True:
	enter = int(input())
	if enter != 0:
		if len(current5Numbers) == 5:
			past5Numbers = current5Numbers[:]
			maxsCollection.append(max(past5Numbers))
			current5Numbers.clear()
		current5Numbers.append(enter)
	else:
		if not len(current5Numbers) in [0, 5]:
			difference = len(past5Numbers) - len(current5Numbers)
			maxsCollection[-1] = max(past5Numbers[:len(past5Numbers) - difference])
		result = max(maxsCollection)
		break
print(result)

# 3 вариант. Умом особо не блещет: сделан по такому же приниципу, что и предыдущий. Ничего путнего конкретно по данному заданию не нашёл.
entersCollection = []
cache = []
while True:
	enter = int(input())
	if enter != 0:
		if len(entersCollection) >= 5:
			if len(cache) % 100 == 0 and cache: # ааааааптимизация (сжатие) кэша раз в 100 подходов. Помогло
				cacheMaximum = max(cache)
				cache.clear()
				cache.append(cacheMaximum)
			cache.append((max(entersCollection), entersCollection[:]))
			entersCollection.clear()
		entersCollection.append(enter)
	else:
		if entersCollection and len(cache[-1]) <= 5:
			(maximum, enters) = cache[-1]
			maximum = max(enters[:len(entersCollection)])
			cache[-1] = (maximum, enters)
		break	
print(max(cache, key=lambda enter: enter[0])[0])