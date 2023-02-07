	# TODO не робит. Проходит только два теста. Не знаю, что делать.
def processWayNumbersForWhiteKing(horse_coord):
	way_number_area = [[0] * 10 for _ in range(10)]
	way_number_area[1][1] = 1
	j_coords_in_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
	horse_i = int(horse_coord[1])
	horse_j = horse_coord[0]
	if horse_j in j_coords_in_alphabet:
		horse_j = j_coords_in_alphabet.index(horse_j) + 1
	for i in range(1, 9):
		for j in range(1, 9):
			if not (horse_i == i and horse_j == j):
				way_number_area[i][j] += way_number_area[i][j - 1] + way_number_area[i - 1][j - 1] + way_number_area[i - 1][j]
	return way_number_area[7][7]

print(processWayNumbersForWhiteKing(input()))