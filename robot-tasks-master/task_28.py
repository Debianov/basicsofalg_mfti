from pyrob.api import *

@task(delay=0.01)
def task_7_6():
   filledCellNumber = 0
   while filledCellNumber < 5:
      move_right()
      if cell_is_filled():
         filledCellNumber += 1

if __name__ == '__main__':
   run_tasks()