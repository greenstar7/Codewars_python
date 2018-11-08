"""Hrynevych Artemii
My second solution for 6 by 6 Skyscrapers kata.
This time using constraints propagation.
https://www.codewars.com/kata/6-by-6-skyscrapers
"""
# This solution is almost 9 time faster then the bruteforce one
# To make this solutions i used these articles:
# -http://norvig.com/sudoku.html
# -https://en.wikipedia.org/wiki/Constraint_satisfaction

def cross(A, B):
    """Helper function to make cross product of two strings."""
    return [''.join((a, b)) for a in A for b in B]

digits = '123456'
rows = 'ABCDEF'
cols = digits
squares = cross(rows, cols)
unitlist = ([cross(row, cols) for row in rows] +
            [cross(rows, col) for col in cols])
units = {s: [u for u in unitlist if s in u] for s in squares}
# units[s][0] -- row with the square s; units[s][1] -- column with the square s
peers = {s: set((units[s][0] + units[s][1])).difference((s,)) for s in squares}

# GRID SIZE
N = 6
# dict of {clue: {distance from clue: set(possible values in cell), next distance:...}, nect clue:... }
# for every clue (1, 2, 3, 4)
POS = {
    1: {0: {6}, 1: {1,2,3,4,5}, 2: {1,2,3,4,5}, 3: {1,2,3,4,5}, 4: {1,2,3,4,5}, 5: {1,2,3,4,5}},
    2: {0: {1,2,3,4,5}, 1: {1,2,3,4,5,6}, 2: {1,2,3,4,5,6}, 3: {1,2,3,4,5,6}, 4: {1,2,3,4,5,6}, 5: {1,2,3,4,5,6}},
    3: {0: {1,2,3,4}, 1: {1,2,3,4,5}, 2: {1,2,3,4,5,6}, 3: {1,2,3,4,5,6}, 4: {1,2,3,4,5,6}, 5: {1,2,3,4,5,6}},
    4: {0: {1,2,3}, 1: {1,2,3,4}, 2: {1,2,3,4,5}, 3: {1,2,3,4,5,6}, 4: {1,2,3,4,5,6}, 5: {1,2,3,4,5,6}},
    5: {0: {1,2}, 1: {1,2,3}, 2: {1,2,3,4}, 3: {1,2,3,4,5}, 4: {1,2,3,4,5,6}, 5: {1,2,3,4,5,6}},
    6: {0: {1}, 1: {2}, 2: {3}, 3: {4}, 4: {5}, 5: {6}},
    0: {0: {1,2,3,4,5,6}, 1: {1,2,3,4,5,6}, 2: {1,2,3,4,5,6}, 3: {1,2,3,4,5,6}, 4: {1,2,3,4,5,6}, 5: {1,2,3,4,5,6}}
}   

TOP_CLUES = None
RIGHT_CLUES = None
BOT_CLUES = None
LEFT_CLUES = None

def solve_puzzle(clues):
    """Main function to solve the 6 by 6 skyscrapers puzzle.
    
    Arguments:
    clues -- tuple of 24 clues going clockwise.
    """
    search_result = search(parse_clues(clues))
    if not search_result:
        return False
    # next piece of code just to convert the result in a suitable form
    # for the codewars tests (return result as 6 tuple of 6 tuples)
    res = []
    temp = []
    for square in squares:
        temp.append(int(search_result[square]))
        if square[1] == str(N):
            res.append(tuple(temp))
            temp = []
    return tuple(res)

def parse_clues(clues):
    """Convert clues into grid as a dict of {square: string}"""
    grid = {s: digits for s in squares}
    global TOP_CLUES
    global RIGHT_CLUES
    global BOT_CLUES
    global LEFT_CLUES
    TOP_CLUES = dict(zip(cols, clues[:N]))
    RIGHT_CLUES = dict(zip(rows, clues[N:2*N]))
    BOT_CLUES = dict(zip(cols, reversed(clues[2*N:3*N])))
    LEFT_CLUES = dict(zip(rows, reversed(clues[3*N:])))
    # Checking every square in grid to simplify possibilities
    for k in grid:
        row = k[0]
        col = k[1]
        top_dist = ord(row) - ord('A')
        left_dist = int(col) - 1
        bot_dist = N-1-top_dist
        right_dist = N-1-left_dist
        clues_intersection = set.intersection(POS[TOP_CLUES[col]][top_dist],
                                              POS[BOT_CLUES[col]][bot_dist],
                                              POS[LEFT_CLUES[row]][left_dist],
                                              POS[RIGHT_CLUES[row]][right_dist])
        grid[k] = ''.join(str(el) for el in clues_intersection)
        
    return grid

def search(values):
    """Using depth-first search and propagation, try all possible values."""
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in squares): 
        return values ## Solved!
    # Chose the unfilled square s with the fewest possibilities
    # min for tuple compares the 0 pos first if there are tuple with the same
    # element on pos 0 in the given iterable, then it compares next positions
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])

def some(seq):
    """Return some element of seq that is true."""
    for e in seq:
        if e: 
            return e
    return False

def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected.
    """
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False
    
def eliminate(values, s, d):
    """Eliminate d from values[s] and propagate further
    Return values, except return False if a contradiction is detected.
    """
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False # Contradiction: removed last value
    # (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    # (2) If a unit u is reduced to only one place for a value d, then put it there.
    for unit in units[s]:
        dplaces = [s for s in unit if d in values[s]]
    if len(dplaces) == 0:
        return False ## Contradiction: no place for this value
    elif len(dplaces) == 1:
	    # d can only be in one place in unit; assign it there
        if not assign(values, dplaces[0], d):
            return False
    # (3) if we filled up row or column:
    # check if it fits the clues
    # if all squares in row have 1 element
    if all(len(values[square])==1 for square in units[s][0]):
        # if this row doesnt fit the clue
        if not check_row_clue(values, units[s][0]):
            return False
    # if all square in column have 1 element
    if all(len(values[square])==1 for square in units[s][1]):
        # if this column foesnt fit the clue
        if not check_col_clue(values, units[s][1]):
            return False

    return values

def check_row_clue(values, row_squares):
    """Function to check if the row satisfies clues"""
    # getting the first char from the first element in the row
    # that is letter of the row
    row_letter = row_squares[0][0]
    
    left_clue = LEFT_CLUES[row_letter]
    if left_clue != 0:
        prev_max = 0
        count = 0
        for square in row_squares:
            if int(values[square]) > prev_max:
                count += 1
                prev_max = int(values[square])
        if count != left_clue:
            return False
        
    right_clue = RIGHT_CLUES[row_letter]
    if right_clue != 0:
        prev_max = 0
        count = 0
        for square in reversed(row_squares):
            if int(values[square]) > prev_max:
                count += 1
                prev_max = int(values[square])
        if count != right_clue:
            return False
        
    return True

def check_col_clue(values, col_squares):
    """Function to check if the column satisfies clues"""
    # getting the second char from the first element in the column
    # that is number of the column
    col_num = col_squares[0][1]

    top_clue = TOP_CLUES[col_num]
    if top_clue != 0:
        prev_max = 0
        count = 0
        for square in col_squares:

            if int(values[square]) > prev_max:
                count += 1
                prev_max = int(values[square])
        if count != top_clue:
            return False
        
    bot_clue = BOT_CLUES[col_num]
    if bot_clue != 0:
        prev_max = 0
        count = 0
        for square in reversed(col_squares):
            if int(values[square]) > prev_max:
                count += 1
                prev_max = int(values[square])
        if count != bot_clue:
            return False
        
    return True
