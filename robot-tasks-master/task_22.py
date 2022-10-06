from pyrob.api import *

@task(delay=0.01)
def task_5_10():
   while True:
      if not wall_is_on_the_right():
         while not wall_is_on_the_right():
            fill_cell()
            move_right()
         fill_cell()
      else:
         while not wall_is_on_the_left():
            fill_cell()
            move_left()
         fill_cell()
         if wall_is_beneath():
            break
      if not wall_is_beneath():
         move_down()

if __name__ == '__main__':
   run_tasks()
