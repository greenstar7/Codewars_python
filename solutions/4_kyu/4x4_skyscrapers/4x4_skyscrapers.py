"""Hrynevych Artemii
My solution for 4 kyu '4 by 4 Skyscrapers' kata
https://www.codewars.com/kata/4-by-4-skyscrapers"""

#https://stackoverflow.com/questions/18872553/skyscraper-puzzle-algorithm

# TODO: try with bruteforce
#Basically, you need to populate NxN squares with integers from 1 to N inclusive, following the following constraints:
# -Each integer appears in every row exactly once
# -Each integer appears in every column exactly once
# -The row "clues" are satisfied
# -The column "clues" are satisfied

# TODO: try constrain satisfaction
# -http://norvig.com/sudoku.html
# -https://en.wikipedia.org/wiki/Constraint_satisfaction


# brute force recursion pseudocode
#def fill_square(board, row, column):
#  if row == column == N-1: # the board is full, we're done
#    print board
#    return
#  next_row, next_col = calculate_next_position(row, col)
#  for value in range(1, N+1):
#    next_board = copy.deepcopy(board)
#    next_board[row][col] = value
#    if is_valid_board(next_board):
#      fill_square(next_board, next_row, next_col)
#
#board = initialize_board()
#fill_square(board, 0, 0)
