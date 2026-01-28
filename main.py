import numpy as np
from sudoku_base import extract_blocks, extract_columns, extract_rows
from basic_solvers import missing_number

def get_input():

    #sudoku = input()
    """
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
    """
    input_sudoku = np.array([
        5, 3, 4, 6, 7, 8, 9, 1, None,  # Chybí 2
        6, 7, 2, 1, 9, 5, 3, 4, None,  # Chybí 8
        1, 9, 8, 3, 4, 2, 5, 6, None,  # Chybí 7
        8, 5, 9, 7, 6, 1, 4, 2, None,  # Chybí 3
        4, 2, 6, 8, 5, 3, 7, 9, None,  # Chybí 1
        7, 1, 3, 9, 2, 4, 8, 5, None,  # Chybí 6
        9, 6, 1, 5, 3, 7, 2, 8, None,  # Chybí 4
        2, 8, 7, 4, 1, 9, 6, 3, None,  # Chybí 5
        3, 4, 5, 2, 8, 6, 1, 7, None  # Chybí 9
    ])
    return input_sudoku


task = get_input()
sudoku_rows = extract_rows(task)
sudoku_columns = extract_columns(task)
sudoku_blocks = extract_blocks(task)

print(sudoku_rows)
print(sudoku_columns)
print(sudoku_blocks)

idx = 0
for a in sudoku_rows:
    new = missing_number(a)
    np.put(sudoku_rows, idx, new)
    idx += 1
