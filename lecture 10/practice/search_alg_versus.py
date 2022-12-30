#%%
import util
from line_search import search
from binary_search import binary_search
from interpolation_search import interpolation_search

util.plot_search_results_small(
	('Линейный поиск', search),
	('Бинарный поиск', binary_search),
	('Интерполяционный поиск', interpolation_search),
)
util.plot_search_results_huge(
	('Бинарный поиск', binary_search),
	('Интерполяционный поиск', interpolation_search),
)