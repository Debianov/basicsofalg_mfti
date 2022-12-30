#%%
import util
import merge_sort

util.plot_sort_results(
	('Первый вариант сортировки слиянием', merge_sort.merge_sort),
	('Альт. вариант сортировки слиянием', merge_sort.alt_merge_sort),
)