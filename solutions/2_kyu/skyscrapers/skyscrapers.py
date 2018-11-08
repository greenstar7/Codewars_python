"""Hrynevych Artemii
My solution for 6 by 6 Skyscrapers kata
https://www.codewars.com/kata/6-by-6-skyscrapers
"""
# This solution is too slow, but sometimes passes with 0.7 seconds
# before timeout xD

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

GRID = [[set(range(1,N+1)) for i in range(N)] for j in range(N)]
TOP_CLUES = None
BOT_CLUES = None
LEFT_CLUES = None
RIGHT_CLUES = None

def solve_puzzle(clues):
    global GRID
    global TOP_CLUES
    global BOT_CLUES
    global LEFT_CLUES
    global RIGHT_CLUES
    # SIMPLIFY as much as I can before bruteforce
    # all clues are going clockwise
    TOP_CLUES = clues[:N]
    RIGHT_CLUES = clues[N:2*N]
    BOT_CLUES = list(reversed(clues[2*N:3*N]))
    LEFT_CLUES = list(reversed(clues[3*N:]))
    # checking possibilities for cells values with clues
    for i in range(N):
        for j in range(N):
            GRID[j][i] = (GRID[j][i].intersection(POS[TOP_CLUES[i]][j])).intersection(POS[BOT_CLUES[i]][N-j-1])
            GRID[i][j] = (GRID[i][j].intersection(POS[LEFT_CLUES[i]][j])).intersection(POS[RIGHT_CLUES[i]][N-j-1])
    # simplifying the grid for cases when number is alone in cell
    # or number is alone in row or column
    changes = True
    while changes:
        changes = False
        for i in range(N):
            for j in range(N):
                for el in GRID[i][j]:
                    if alone((i, j), el):
                        changes = delete_from_cross((i,j), el) or changes
                        GRID[i][j] = (el,)
    # BRUTEFORCE
    puzzle = [[el[0] if len(el) == 1 else 0 for el in line] for line in GRID]
    unknown = [(row, col) for row in range(N) for col in range(N) if not puzzle[row][col]]
    curr_index = 0
    while curr_index < len(unknown):
        curr_pos = unknown[curr_index]
        puzzle[curr_pos[0]][curr_pos[1]] +=1
        # if we got to the end of the available variants
        if puzzle[curr_pos[0]][curr_pos[1]] > N:
            # zeroing the current cell
            puzzle[curr_pos[0]][curr_pos[1]] = 0
            # moving to the previous one
            curr_index -= 1
            continue
        elif puzzle[curr_pos[0]][curr_pos[1]] not in GRID[curr_pos[0]][curr_pos[1]]:
            continue
        # if number we inserted is valid
        elif is_valid(puzzle, curr_pos):
            # moving to the next empty cell
            curr_index += 1
            continue
        # if number in cell is still in range 1 - N
        # but cell is not valid yet, then we just continue
        else:
            continue 
    puzzle = tuple([tuple(line) for line in puzzle])
    GRID = [[set(range(1,N+1)) for i in range(N)] for j in range(N)]
    return puzzle

def is_valid(grid, pos):
    # check if unique in the row and col (cross)
    el = grid[pos[0]][pos[1]]
    for i in range(N):
        if i != pos[1]:
            if el == grid[pos[0]][i]:
                return False
        if i != pos[0]:
            if el == grid[i][pos[1]]:
                return False
    # check if satisfies clues
    # check top clues
    clue = TOP_CLUES[pos[1]]
    if clue != 0:
        prev_max = 0
        count = 0
        zero = False
        for i in range(N):
            if grid[i][pos[1]] == 0:
                zero = True
            if grid[i][pos[1]] > prev_max:
                count += 1
                prev_max = grid[i][pos[1]]
        if not zero and count != clue:
            return False
    # check right clues
    clue = RIGHT_CLUES[pos[0]]
    if clue != 0:
        prev_max = 0
        count = 0
        zero = False
        for i in range(N-1,-1,-1):
            if grid[pos[0]][i] == 0:
                zero = True
                break
            if grid[pos[0]][i] > prev_max:
                count += 1
                prev_max = grid[pos[0]][i]
        if not zero and count != clue:
            return False
    # check bot horizontal clues
    clue = BOT_CLUES[pos[1]]
    if clue != 0:
        prev_max = 0
        count = 0
        zero = False
        for i in range(N-1,-1,-1):
            if grid[i][pos[1]] == 0:
                zero = True 
                break
            if grid[i][pos[1]] > prev_max:
                count += 1
                prev_max = grid[i][pos[1]]
        if not zero and count != clue:
            return False
    # check left clues
    clue = LEFT_CLUES[pos[0]]
    if clue != 0:
        prev_max = 0
        count = 0
        zero = False
        for i in range(N):
            if grid[pos[0]][i] == 0:
                zero = True
                break
            if grid[pos[0]][i] > prev_max:
                count += 1
                prev_max = grid[pos[0]][i]
        if not zero and count != clue:
            return False
    return True
    
    
def alone(pos, el):
    if len(GRID[pos[0]][pos[1]]) == 1:
        return True
    not_in_row = True
    not_in_col = True
    for i in range(N):
        if i != pos[1]:
            if el in GRID[pos[0]][i]:
                not_in_row = False
        if i != pos[0]:
            if el in GRID[i][pos[1]]:
                not_in_col = False
    return not_in_col or not_in_row

def delete_from_cross(pos, el):
    deleted = False
    for i in range(N):
        if i != pos[1]:
            if el in GRID[pos[0]][i]:
                GRID[pos[0]][i].remove(el)
                deleted = True
        if i != pos[0]:
            if el in GRID[i][pos[1]]:
                GRID[i][pos[1]].remove(el)
                deleted = True
    return deleted