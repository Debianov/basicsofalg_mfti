# 	# TODO как насчёт ООП?

truck_weight = int(input())
platform_height = int(input())
piano_weight = int(input())
piano_height = int(input())
fridge_weight = int(input())
fridge_height= int(input())
bridge_weight_limit = int(input())
tunnel_height_limit = int(input())
max_height = fridge_height if fridge_height > piano_height else piano_height

# 1 вариант
if fridge_height + platform_height <= tunnel_height_limit and truck_weight + piano_weight + fridge_weight <= bridge_weight_limit:
	print("YES")
elif max_height + platform_height <= tunnel_height_limit and truck_weight + piano_weight <= bridge_weight_limit:
	print("YES")
else:
	print("NO")

# 2 вариант
if truck_weight + piano_weight <= bridge_weight_limit:
	if max_height + platform_height <= tunnel_height_limit:
		print("YES")
	elif fridge_height + platform_height <= tunnel_height_limit and truck_weight + piano_weight + fridge_weight <= bridge_weight_limit:
		print("YES")
	else:
		print("NO")
else:
	print("NO")