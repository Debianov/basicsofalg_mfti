from pyrob.api import *

@task(delay=0.01)
def task_8_27():
   while not cell_is_filled():
      move_up()
   else:
      move_right()
      if not cell_is_filled():
         move_left(2)

if __name__ == '__main__':
   run_tasks()
