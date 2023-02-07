def make_exchange(money, coins):
	ways_to_sums = [0] * (money + 1)
	ways_to_sums[0] = 1 # типа чтобы достичь нулевой суммы, нужен один способ. Но
	# это когда у нас есть монета с нулевым номиналом. А явно она не прописана.
	# Тем не менее...
	for current_index_coin in range(len(coins)):
		for current_sum in range(len(ways_to_sums)):
			if coins[current_index_coin] <= current_sum: # логично предположить, что
				# монета участвует в процессе размена только если её номинал меньше
				# или равен разменной сумме.
				ways_to_sums[current_sum] += ways_to_sums[current_sum - coins[current_index_coin]] # сумма = одна монета + вторая монета. Чтобы найти неизвестное, надо... смотрите в источнике.
	return ways_to_sums[money]