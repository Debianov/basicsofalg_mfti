from pyrob.api import *

@task(delay=0.01)
def task_8_2():
   while True:
      if (wall_is_above() and not wall_is_beneath()) or (not wall_is_above() and wall_is_beneath()):
         fill_cell()
      if not wall_is_on_the_right():
         move_right()
      else:
         break

if __name__ == '__main__':
   run_tasks()
