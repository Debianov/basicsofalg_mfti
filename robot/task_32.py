from pyrob.api import *

def walk_upstairs():
   cilledCellsNumber = 0
   while not wall_is_above():
      move_up()
      if cell_is_filled():
         cilledCellsNumber += 1
      else:
         fill_cell()
   while not wall_is_beneath():
      move_down()
   return cilledCellsNumber

@task(delay=0.01)
def task_8_18():
   cilledCellsNumber = 0
   while not wall_is_on_the_right():
      if wall_is_above():
         if cell_is_filled():
            cilledCellsNumber += 1
         else:
            fill_cell()
      else:
         cilledCellsNumber += walk_upstairs()
      move_right()
   mov('ax', cilledCellsNumber) #? было бы неплохо их здесь применить, иначе смысл от подобного условия задания? Научиться вызывать функции? Или объяснили 
   #? тогда хотяб, для чего они нужны.

if __name__ == '__main__':
   run_tasks()