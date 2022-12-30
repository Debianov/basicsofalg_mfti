#%%
import util
import bubble_sort

util.plot_bubble_sort_results(
	('Обычная реализация', bubble_sort.bubble_sort),
	('Реализация с проверкой на отсортированность', bubble_sort.bubble_sort_adaptive)
)