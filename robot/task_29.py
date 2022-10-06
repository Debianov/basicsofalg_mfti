from pyrob.api import *

@task(delay=0.01)
def task_7_7():
   filledInRowCellNumber = 0
   while filledInRowCellNumber < 3 and not wall_is_on_the_right():
      move_right()
      if cell_is_filled():
         filledInRowCellNumber += 1
      else:
         filledInRowCellNumber = 0

if __name__ == '__main__':
   run_tasks()
