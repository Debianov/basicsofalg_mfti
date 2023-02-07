"""
Дано N предметов. Каждый из них имеет вес w i и стоимость p i . Также имеется рюкзак вместимостью W. От вас требуется найти такой набор предметов, 
что их суммарная стоимость максимальна, а суммарный вес не превосходит вместимость рюкзака. Ответом на задау надо будет вывести стоимость такого набора.
"""

def backpack_capacity(N, W, things):
	max_price_for_W = [[0] * (W + 1) for _ in range(N + 1)]
	for thing_index in range(1, N + 1):
		for W_index in range(1, W + 1):
			if things[thing_index - 1][0] > W_index:
				max_price_for_W[thing_index][W_index] = max_price_for_W[thing_index - 1][W_index] # не кладём.
			else:
				max_price_for_W[thing_index][W_index] = max(max_price_for_W[thing_index - 1][W_index],
				max_price_for_W[thing_index - 1][W_index - things[thing_index - 1][0]] + things[thing_index - 1][1]) # класть вещь, или нет?
	for i in range(N + 1):
		for j in range(W + 1):
			print(max_price_for_W[i][j], end=" ")
		print()
	return max_price_for_W[-1][-1]

N = int(input())
W = int(input())
things = []
for enter in range(N * 2):
	things.append(int(input()))
	if not enter % 2 == 0:
		p, w = things.pop(), things.pop()
		things.append((w, p))

print(backpack_capacity(N, W, things))