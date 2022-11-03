	#! последние два теста также не проходит, но там вообще какой-то пред на входе и ожидаемом результате.

S = input()
k = int(input())
wordCombine = ""
for (iter, word) in enumerate(S):
	if S.index(word) == 0 and iter != 0:
		if not S[iter:iter + len(wordCombine)] in wordCombine:
			wordCombine += word
			continue
		else:
			break
	else:
		wordCombine += word

kOfS = len(S) // len(wordCombine)
if k < 0: 
	wordCombineNumber = (kOfS - abs(k) + 1)
	if wordCombineNumber >= 0:
		print(S[0:wordCombineNumber * len(wordCombine)])
	else:
		print("NO SOLUTION")
if k > 0:
	result = ""
	for _ in range(k):
		result += S
	print(result)