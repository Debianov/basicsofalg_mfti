#%%
import util
import matplotlib
import random
import math

def recursive_fib(n):
	if n <= 1:
		return n
	return recursive_fib(n - 1) + recursive_fib(n - 2)

assert recursive_fib(0) == 0
assert recursive_fib(1) == 1
assert recursive_fib(9) == 34

def recursive_fib_with_cache(n, cache=None):
	cache = cache if cache else [0, 1]
	if n <= 1:
		return n
	a_sum = recursive_fib_with_cache(n - 1, cache) + recursive_fib_with_cache(n - 2, cache)
	return a_sum

assert recursive_fib_with_cache(0) == 0
assert recursive_fib_with_cache(1) == 1
assert recursive_fib_with_cache(9) == 34

def fib(n):
	fib_list = [0, 1]
	if n <= 1:
		return n
	for current_n in range(2, n + 1):
		fib_list.append(fib_list[current_n - 1] + fib_list[current_n - 2])
	return fib_list[n]

assert fib(0) == 0
assert fib(1) == 1
assert fib(9) == 34

if __name__ == "__main__":
	util.plot_fib_results(
		('Рекурсивная реализация', recursive_fib),
		('Рекурсивная реализация с кэшем', recursive_fib_with_cache),
		('Реализация при помощи цикла', fib)
	)