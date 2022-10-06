from pyrob.api import *

def moveToStartPosition():
   move_down()
   move_right()

def moveToNextLayer():
   move_down(4)

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

@task(delay=0.001)
def task_2_4():
   moveToStartPosition()
   for externalForPosition in range(5):
      for innerForPosition in range(10):
         drawStar()
         if not innerForPosition == 9:
            if externalForPosition % 2 == 0:
               move_right(4)
            else:
               move_left(4)
      if not externalForPosition == 4:
         moveToNextLayer()
      else:
         move_left((4 * 9) + 1)
         move_up()

if __name__ == '__main__':
   run_tasks()
