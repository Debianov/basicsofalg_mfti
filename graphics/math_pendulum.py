	# TODO Памагити

import graphics as gr
import math as m
import time

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)


# f (сила возвращающая) = mgsina, где a — угол отклонения, mg — сила тяжести.
# x = A * sin(w0t + a), где a нач. фаза колебаний, w0 циклическая частота колебаний
# маятник движется по дуге окружности радиуса L
# a = s/l угол отклонения = длина стягивающей дуги / радиус