""""
    Code to solve a Sudoku Puzzle using the backtracking algorithm.
    Input:
"""
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
"""
    In this input, the 0s represent the numbers that are missing from the puzzle.
    
    Written by Rodrigo Almeida (rpa299)    
"""

# print function
def printBoard(board):
    for row in range(9):
        for col in range(9):
            print(board[row][col], end = " ")
        print()

#check row
#   true if valid
#   false if invalid
def checkRow(board, row, valueAttempt):
    for col in range(9):
        if(valueAttempt == board[row][col]):
            return False
    return True

#check coll
#   true if value
#   false if invalid
def checkCol(board, col, valueAttempt):
    for row in range(9):
        if(valueAttempt == board[row][col]):
            return False
    return True

#check block
#   true if valid
#   false if invalid
