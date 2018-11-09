"""Hrynevych Artemii
My solution for 2 kyu 'Hard Sudoku Solver' kata
https://www.codewars.com/kata/hard-sudoku-solver-1/
based on http://norvig.com/sudoku.html article
"""

def cross(A, B):
    """Helper function to get cross product"""
    return [''.join((a, b)) for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
unitlist = ([cross(rows, col) for col in cols] +
            [cross(row, cols) for row in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = {s: [u for u in unitlist if s in u] for s in squares}
peers = {s: set(sum(units[s],[])).difference((s,)) for s in squares}
RESULTS = []

def sudoku_solver(grid):
    """Main function to solve the sudoku puzzle.
    
    Arguments:
    grid -- 9x9 list of sudoku puzzle squares values
    """
    global RESULTS
    RESULTS = []
    # if grid contains not allowed symbols or has wrong dimensions
    if not is_valid(grid):
        print('not valid')
        raise
    # searching for solution
    search(parse_grid(grid))
    # if we have multiple solution, than grid is not valid as well
    assert len(RESULTS) == 1
    # convert result in needed format for codewars tests
    values = RESULTS[0]
    res = []
    temp = []
    for square in squares:
        temp.append(int(values[square]))
        if square[1] == str(9):
            res.append(temp)
            temp = []
    return res

def search(values):
    """Function to search solutions for the grid.
    Using depth-first search and propagation, try all possible values.
    """
    global RESULTS
    
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in squares):
        if values not in RESULTS:
            RESULTS.append(values)
        return False
    # Chose the unfilled square s with the fewest possibilities
    # min for tuple compares the 0 pos first if there are tuple with the same
    # element on pos 0 in the given iterable, then it compares next positions
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])

def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    ## To start, every square can be any digit; then assign values from the grid.
    values = {s: digits for s in squares}
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False ## (Fail if we can't assign d to square s.)
    return values

def grid_values(grid):
    """Convert grid into a dict of {square: char} with '0' or '.' for empties."""
    chars = [str(num) for row in grid for num in row if str(num) in digits or str(num) in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False
    
def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
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
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
    if len(dplaces) == 0:
        return False ## Contradiction: no place for this value
    elif len(dplaces) == 1:
	    # d can only be in one place in unit; assign it there
        if not assign(values, dplaces[0], d):
            return False
    return values

def is_valid(grid):
    """Function to check basic corectness of the grid"""
    N = 9
    if len(grid) != N:
        return False
    for row in grid:
        if len(row) != N:
            return False
    if all(el!=0 for el in row for row in grid):
        return False
    return True

def some(seq):
    """Return some element of seq that is true."""
    for e in seq:
        if e: return e
    return False