from pyrob.api import *

def moveToStartPosition():
   move_down(2)
   move_right(2)

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

@task
def task_2_1():
   moveToStartPosition()
   drawStar()
   moveToFinishPosition()

if __name__ == '__main__':
   run_tasks()
