from pyrob.api import *

@task
def task_5_2():
   while wall_is_beneath():
      move_right(1)

if __name__ == '__main__':
   run_tasks()