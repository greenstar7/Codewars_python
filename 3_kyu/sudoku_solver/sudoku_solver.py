"""Hrynevych Artemii
My solution for the Codewars "Sudoku Solver" kata
https://www.codewars.com/kata/5296bc77afba8baa690002d7
"""

N = 9 # now only suitable for 9x9 sudoku

def sudoku(puzzle):
    """Function that returns the solved sydoku puzzle
    as a 2d array of 9 x 9 sudoku cells
    
    Function assume that all given sudoku grids will be correct,
    will be "easy" (i.e. determinable - there will be no need to assume
    and test possibilities on unknowns) 
    and can be solved with a brute-force approach.
    
    Arguments:
    puzzle -- 2d array representing sudoku puzzle to solve
    """
    # a list of cell for us to fullfil with a valid number
    unknown = [(y, x) for y in range(N) for x in range(N) if puzzle[y][x]==0]
    # starting from the first empty cell
    curr_index = 0
    # while we are not filled all empty cells
    # with a valid number
    while 0 <= curr_index < len(unknown):
        curr_pos = unknown[curr_index]
        puzzle[curr_pos[0]][curr_pos[1]] +=1
        # if nums from 1 to 9 are not valid
        # that means we need to change previous cell
        if puzzle[curr_pos[0]][curr_pos[1]] > 9:
            # zeroing the current cell
            puzzle[curr_pos[0]][curr_pos[1]] = 0
            # moving to the previous one
            curr_index -= 1
        # if number we inserted is valid
        elif is_valid(puzzle, (curr_pos[0],curr_pos[1])):
            # moving to the next empty cell
            curr_index += 1
        # if number in cell is still in range 1-9
        # but not valid yet, then we just continue
        else:
            continue        
    return puzzle

def is_valid(puzzle, pos):
    """Function to check if the value 
    in the puzzle on the given position is valid
    
    Arguments:
    puzzle -- 2d 9x9 sudoku grid
    pos -- position of the value to check
    """
    pos_number = puzzle[pos[0]][pos[1]]
    row = pos[0]
    for col in range(N):
        if puzzle[row][col] == pos_number:
            if (row, col) != pos:
                return False
    # check column
    col = pos[1]
    for row in range(N):
        if puzzle[row][col] == pos_number:
            if (row, col) != pos:
                return False
    # check square
    # 3*(pos[0]//3) -- upper bound of the square
    # XXX
    # ***
    # ***
    upper_bound = 3*(pos[0]//3)
    # 3*(pos[1]//3) -- left bound of the square
    # X**
    # X**
    # X**
    left_bound = 3*(pos[1]//3)
    for row in range(upper_bound, upper_bound+3):
        for col in range(left_bound, left_bound+3):
            if puzzle[row][col] == pos_number:
                if (row, col) != pos:
                    return False
    return True