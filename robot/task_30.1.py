"""
Авторский первый вариант решения.

Решил заморочиться и сделать через выделение клеток строками, пропуская вычисляемые заранее клетки, который должны быть пустыми.

Да, я знаю, что есть очень простое решение. Меня оно не интересует.
"""

from pyrob.api import *

k = 0

def squareSizeEvaluation():
   squareLength = 1
   squareWidth = 1
   while not wall_is_beneath():
      move_down()
      squareLength += 1
      squareWidth += 1
   move_up(squareLength - 1) # возврат в начальную позицию.
   return (squareLength, squareWidth)

def notFillCellsDefine(squareWidth, middleSquare):
   k = squareWidth + 1
   yield "Initial"
   stringNumber = 0
   while True:
      if stringNumber <= middleSquare:
         k -= 2
         notFillCell = (stringNumber, stringNumber  + k)
         stringNumber = yield notFillCell
      elif stringNumber > middleSquare and stringNumber < squareWidth:
         k += 2
         notFillCell = (stringNumber - k, stringNumber)
         stringNumber = yield notFillCell
      else:
         break
   raise StopIteration

def additionalValuesCalculating(squareLength, squareWidth):
   middleSquare = squareLength // 2
   lastNumberString = squareWidth - 1
   lastCellPosition = squareLength - 1
   return (middleSquare, lastNumberString, lastCellPosition)

def draw(squareLength, squareWidth):
   (middleSquare, lastNumberString, lastCellPosition) = additionalValuesCalculating(squareLength, squareWidth)
   notFillCellsList = []
   notFillCellGenerator = notFillCellsDefine(squareWidth, middleSquare)
   next(notFillCellGenerator)
   for stringNumber in range(squareWidth):
      notFillCell = notFillCellGenerator.send(stringNumber)
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
   notFillCellGenerator.close()

@task(delay=0.01)
def task_9_3():
   global k
   (squareLength, squareWidth) = squareSizeEvaluation()
   draw(squareLength, squareWidth)

if __name__ == '__main__':
   run_tasks()