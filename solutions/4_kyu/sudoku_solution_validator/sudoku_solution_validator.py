''' Hrynevych Artemii
My solution for the Codewars "Sudoku Solution Validator" kata
https://www.codewars.com/kata/sudoku-solution-validator/'''

def validSolution(board):
    ''' Function to check whether the 9x9 sudoku board
    is solved correctly'''
    right = sum(list(range(1,10)))
    # check rows
    for i in range(9):
        if sum(board[i]) != right:
            return False
    # check columns
    for i in range(9):
        s = 0
        for j in range(9):
            s+= board[j][i]
        if s != right: 
            return False
    # check squares
    for i in range(0,9,3):
        for j in range(0,9,3):
            s = 0
            s += board[i][j]+board[i][j+1]+board[i][j+2]
            s += board[i+1][j]+board[i+1][j+1]+board[i+1][j+2]
            s += board[i+2][j]+board[i+2][j+1]+board[i+2][j+2]
            if s != right:
                return False
    # if all previous checks were not faulty
    # then our board is solved correctly
    return True