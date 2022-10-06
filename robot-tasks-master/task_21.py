from pyrob.api import *

@task(delay=0.01)
def task_4_11():
    move_down()
    move_right()
    for positionTopFor in range(13):
        for _ in range(1 + positionTopFor):
            fill_cell()
            move_right()
        move_down()
        move_left(1 + positionTopFor)

if __name__ == '__main__':
    run_tasks()
