	#! тесты не проходятся, хотя при вводе тех же самых входных данных всё работает, как должно быть в результате. Хз, в чём прикол.
N = int(input())
results = {}
for _ in range(N):
	word = input()
	index = len(word)
	keyCollection = results.get(index)
	if keyCollection:
		keyCollection.append(word)
		keyCollection.sort(key=lambda enter: enter[0], reverse=True)
		results[index] = keyCollection
	else:
		results[index] = [word]

results = dict(sorted(results.items(), key=lambda enter: enter[0]))
for (key, collection) in results.items():
	print(key)
	for value in collection:
		print(value[::-1], value)