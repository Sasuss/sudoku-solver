import numpy as np
from sudoku_base import extract_blocks, extract_columns, extract_rows


def get_input():
    #sudoku = input()
    input_sudoku = np.array([
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
    #side = get_side(sudoku)

    return input_sudoku


task = get_input()
sudoku_rows = extract_rows(task)
sudoku_columns = extract_columns(task)
sudoku_blocks = extract_blocks(task)

print(sudoku_rows)
print(sudoku_columns)
print(sudoku_blocks)

#print(get_input())
