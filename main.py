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


# displays a sudoku grid
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

def is_board_valid(board, pos, num):
    # check column
    for i in range(len(board)):
        if (board[i][pos[1]] == num) and (pos[1] = != i):
            return False

    # check row
    for i in range(len(board[0])):
        if (board[pos[0]][i] == num) and (pos[i] != i):
            return False
    
    # check box (3x3)
    box_x, box_y = pos[1]//3, pos[0]//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if ((i, j) != pos) and (board([i][j]) == num):
                return False
    
    return True



# finds an empty square on the grid
def find_empty_square(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # row, column
                return (i, j)
    return None
