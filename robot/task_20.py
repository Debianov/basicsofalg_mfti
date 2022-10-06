from pyrob.api import *

@task(delay=0.01)
def task_4_3():
   for _ in range(6):
      for positionRightFor in range(28):
         move_right()
         if not positionRightFor == 27:
            fill_cell()
      move_down()
      for positionLeftFor in range(28):
         move_left()
         if not positionLeftFor == 27:
            fill_cell()
      move_down()
   move_right()

if __name__ == '__main__':
   run_tasks()
