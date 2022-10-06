from pyrob.api import *

def moveToStartPosition():
   move_right()
   fill_cell()

@task(delay=0.01)
def task_7_5():
   interval = 1
   moveToStartPosition()
   while not wall_is_on_the_right():
      for _ in range(interval):
         if not wall_is_on_the_right():
            move_right()
         else:
            break
      if not wall_is_on_the_right():
         fill_cell()
         interval += 1

if __name__ == '__main__':
   run_tasks()
