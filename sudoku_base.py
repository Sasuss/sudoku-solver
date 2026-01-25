import math
import numpy as np
from numpy import ndarray

"""
Library for functions used to solve the default version of sudoku (9x9 grid, 3x3 blocks)
"""


def extract_blocks(sudoku: ndarray) -> ndarray:
    blocks = []
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            block = []
            for i in range(3):
                start = (r + i) * 9 + c
                block.extend(sudoku[start: start + 3])
            blocks.append(block)
    blocks = np.array(blocks)
    return blocks


def extract_rows(sudoku: ndarray) -> ndarray:
    """
    :param sudoku: 1d ndarray of sudoku
    :return: ndarraay of inidividual rows from the sudoku
    """
    side = get_side(sudoku)
    rows = []
    for a in range(side):
        row = sudoku[a * side:(a + 1) * side]
        rows.append(row)

    rows = np.array(rows)
    return rows


def extract_columns(sudoku: ndarray) -> ndarray:
    """
    :param sudoku: 1d ndarray of sudoku
    :return: ndarraay of inidividual columns from the sudoku
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


def get_side(sudoku: ndarray) -> int:
    """
    Counts the length of one sudoku side, more usefull imn future use for sudokus of different sizes
    :param sudoku: 1d ndarraay of sudoku
    :return:
    """
    side = math.sqrt(len(sudoku))
    if side % 1 != 0 and side * side != len(sudoku):
        return 0
    side = int(side)
    return side
