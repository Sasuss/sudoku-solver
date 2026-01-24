import numpy as np
import math


def extract_rows(sudoku):
    """
    :param sudoku: 1d list of sudoku
    :return: list of inidividual rows from the sudoku
    """
    side = get_side(sudoku)
    rows = []
    for a in range(side):
        row = sudoku[a * side:(a + 1) * side]
        rows.append(row)

    rows = np.array(rows)
    return rows


def extract_columns(sudoku):
    """
    :param sudoku: 1d list of sudoku
    :return: list of inidividual columns from the sudoku
    """
    side = get_side(sudoku)
    columns = []
    column = []
    for a in range(side):
        for b in range(side):
            column.append(sudoku[a + (b * 9)])

        columns.append(column)
        column = []

    columns = np.array(columns)
    return columns


def get_side(sudoku):
    side = math.sqrt(len(sudoku))
    if side % 1 != 0 and side * side != len(sudoku):
        return "Not a valid sudoku"
    side = int(side)
    return side


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
print(extract_columns(task))

#print(get_input())
