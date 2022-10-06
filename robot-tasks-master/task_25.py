from pyrob.api import *

def moveToStartPosition():
   move_down(2)
   move_right()

def moveToFinishPosition():
   move_up()
   move_left()

def drawStar():
   fill_cell()
   move_right()
   fill_cell()
   move_left()
   move_up()
   fill_cell()
   move_down()
   move_left()
   fill_cell()
   move_right()
   move_down()
   fill_cell()
   move_up()

@task(delay=0.01)
def task_2_2():
   moveToStartPosition()
   drawStar()
   for _ in range(4):
      move_right(4)
      drawStar()
   moveToFinishPosition()

if __name__ == '__main__':
   run_tasks()
