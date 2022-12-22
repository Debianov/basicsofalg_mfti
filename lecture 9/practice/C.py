N = input()
answers = list(map(int, input().split()))

# 0 — лжец, 1 — рыцарь.
# 1 вариант
current_person_type = first_person_type = 0
knights_count_in_1_variant = 0
for answer in answers:
	current_person_type = abs(answer - 1) if current_person_type == 0 else answer
	knights_count_in_1_variant += current_person_type
	current_person_type = current_person_type

# 2 вариант
current_person_type = first_person_type = 1
knights_count_in_2_variant = 0
for answer in answers:
	current_person_type = abs(answer - 1) if current_person_type == 0 else answer
	knights_count_in_2_variant += current_person_type
	current_person_type = current_person_type

print(min(knights_count_in_1_variant, knights_count_in_2_variant))