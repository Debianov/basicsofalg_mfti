enter = list(map(int, input().split()))
price = money = enter[0]
delta = enter[1]
m = enter[2]
current_m = 0
current_day = 1

while current_m != m:
	if current_day == 7:
		current_day = 0
		current_m += 1
	else:
		current_day += 1
		price = price + delta
		money += price

print(money)