"""
 SUDOKU SOLVER WITH BACKTRACKING ~ LIAM HALPIN
 
 Steps:
   1) Pick an empty square;
   2) Try numbers 1 to 9;
   3) Repeat (1) and (2) until a valid number is found;
   4) As soon as we get to a state where the grid is an
      invalid solution, backtrack to previous step;
   5) Retry from (2).
"""

import time  # used for timing solver

"""
 board: the sudoku grid to solve

 Recursive function that backtracks to the previous step
 when board is invalid
"""
def solve(board):
    find = find_empty_square(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if is_board_valid(board, (row, col), i):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

"""
 board: the sudoku grid
 pos: a square on the grid
 num: the guess for the current square (1 to 9)

 Checks if the given board is a valid sudoku grid
"""
def is_board_valid(board, pos, num):
    # Check each column for validity
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
            
    # Check each row for validity
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check each 3x3 for validity
    box_x, box_y = pos[1]//3, pos[0]//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

"""
 board: the sudoku grid

 Finds an empty square on the sudoku grid
"""
def find_empty_square(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # row, column
                return (i, j)
    return None

"""
 board: the sudoku grid

 Displays a sudoku grid
"""
def print_board(board):
    for i in range(len(board)):
        if (i % 3 == 0) and (i != 0):
            print("------------------------")
        for j in range(len(board[0])):
            if (j % 3 == 0) and (j != 0):
                print(" | ", end="")
            
            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end="")


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solving the grid
timeBefore = time.time()
solve(board)
timeAfter = time.time()

totalTime= round(timeAfter-timeBefore, 2)

# Output
print("\n")
print_board(board)
print("Completed in " + str(timeTotal) + " seconds")