import numpy as np
import math




def get_input():
    #sudoku = input()
    sudoku = np.array([
        5, 3, None, None, 7, None, None, None, None,
        6, None, None, 1, 9, 5, None, None, None,
        None, 9, 8, None, None, None, None, 6, None,
        8, None, None, None, 6, None, None, None, 3,
        4, None, None, 8, None, 3, None, None, 1,
        7, None, None, None, 2, None, None, None, 6,
        None, 6, None, None, None, None, 2, 8, None,
        None, None, None, 4, 1, 9, None, None, 5,
        None, None, None, None, 8, None, None, 7, 9
    ])
    side = math.sqrt(len(sudoku))
    if side % 1 != 0 and side * side != len(sudoku):
        return "Not a valid sudoku"

    side = int(side)

    rows = np.array(
        [
            sudoku[0:side]
        ]
    )

    return "sudoku: " + str(sudoku) + "Rows: " + str(rows)


print(get_input())


