# TODO второй способ.

"""
Решил заморочиться и сделать через выделение клеток строками, пропуская вычисляемые заранее клетки, который должны быть пустыми. Планирую попробовать
ещё один способ покороче.

Да, я знаю, что есть очень простое решение. Меня оно не интересует.
"""

from pyrob.api import *

squareLength = 1
squareWidth = 1
k = 0

def squareSizeEvaluation():
   global squareLength, squareWidth
   while not wall_is_beneath():
      move_down()
      squareLength += 1
      squareWidth += 1
   move_up(squareLength - 1) # возврат в начальную позицию.

def coeffCalculating(stringNumber, middleSquare):
   global k
   if stringNumber <= middleSquare:
      k -= 2
      notFillCell = (stringNumber, stringNumber  + k)
   elif stringNumber > middleSquare:
      k += 2
      notFillCell = (stringNumber - k, stringNumber)
   return notFillCell

def additionalValuesCalculating():
   middleSquare = squareLength // 2
   lastNumberString = squareWidth - 1
   lastCellPosition = squareLength - 1
   return (middleSquare, lastNumberString, lastCellPosition)

def draw():
   (middleSquare, lastNumberString, lastCellPosition) = additionalValuesCalculating()
   notFillCellsList = []
   for stringNumber in range(squareWidth):
      notFillCell = coeffCalculating(stringNumber, middleSquare)
      notFillCellsList.append(notFillCell)
      for cellPosition in range(squareLength):
         (notFillLeftCellPosition, notFillRightCellPosition) = notFillCellsList[stringNumber]
         if not cellPosition == notFillLeftCellPosition and not cellPosition == notFillRightCellPosition:
            fill_cell()
         if not stringNumber % 2 == 0 and not wall_is_on_the_left():
            move_left()
         elif stringNumber % 2 == 0 and not wall_is_on_the_right():
            move_right()
      if stringNumber == lastNumberString: 
         move_left(lastCellPosition) # если последняя строка, то вернуть к точке в левой части.
      else:
         move_down() # иначе перейти на следующую строку.

@task(delay=0.01)
def task_9_3():
   global squareLength, squareWidth, k
   squareSizeEvaluation()
   k = squareWidth + 1
   draw()
   squareLength = 1
   squareWidth = 1
   k = 0

if __name__ == '__main__':
   run_tasks()
