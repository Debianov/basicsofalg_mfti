from pyrob.api import *

@task(delay=0.01)
def task_8_29():
   while True:
      while not wall_is_on_the_left() and wall_is_above():
         move_left()
      while not wall_is_on_the_right() and wall_is_above():
         move_right()
      if wall_is_above():
         break
      while not wall_is_above():
         move_up()
      while not wall_is_on_the_left():
         move_left()
      break

if __name__ == '__main__':
   run_tasks()