# TODO везде убрать shebang, проверить табуляцию, посмотреть нейминги ещё раз.

from pyrob.api import *

@task
def task_1_1():
   move_right(2)
   move_down()

if __name__ == '__main__':
   run_tasks()