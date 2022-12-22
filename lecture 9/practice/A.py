enter = input()
enter = enter.split()
result = hex(int(enter[0], 16) ^ int(enter[1], 16))
print(result[2:])