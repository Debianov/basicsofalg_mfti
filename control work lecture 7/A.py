	# TODO как насчёт ООП?
	# TODO недореш

truckWeight = 0
truckPlatformHeight = 0
pianoWeight = 0
pianoHeight = 0
fridgeWeight = 0
fridgeHeight = 0
maxWeightForBridge = 0
maxHeightForTunnel = 0

for var in range(8):
	enter = int(input())
	match var:
		case 0:
			truckWeight = enter
		case 1:
			truckPlatformHeight = enter
		case 2:
			pianoWeight = enter
		case 3:
			pianoHeight = enter
		case 4:
			fridgeWeight = enter
		case 5:
			fridgeHeight = enter
		case 6:
			maxWeightForBridge = enter
		case 7:
			maxHeightForTunnel = enter

print(truckWeight + pianoWeight + fridgeWeight, maxWeightForBridge)
print(truckPlatformHeight + pianoHeight + fridgeHeight, maxHeightForTunnel)
if (truckWeight + pianoWeight + fridgeWeight <= maxWeightForBridge) and (truckPlatformHeight + pianoHeight + fridgeHeight <= maxHeightForTunnel):
	print("YES")
else:
	print("NO")