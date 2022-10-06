from pyrob.api import *

@task(delay=0.01)
def task_5_4():
   while not wall_is_beneath():
      move_down()
   while wall_is_beneath():
      move_right()
   move_down()
   move_left()
   while wall_is_above() and not wall_is_on_the_left():
      move_left()

if __name__ == '__main__':
   run_tasks()
