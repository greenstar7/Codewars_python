"""Hrynevych Artemii
My solution for 4 kyu '4 by 4 Skyscrapers' kata
https://www.codewars.com/kata/4-by-4-skyscrapers"""

# TODO: try constrain satisfaction
# -http://norvig.com/sudoku.html
# -https://en.wikipedia.org/wiki/Constraint_satisfaction

# GRID SIZE
N = 4
# dict of {clue: {distance from clue: set(possible values in cell), next distance:...}, nect clue:... }
# for every clue (1, 2, 3, 4)
POSSIBILITIES = {
    1: {0: {4}, 1: {1,2,3}, 2: {1,2,3}, 3: {1,2,3}},
    2: {0: {1,2,3}, 1: {1,2,3,4}, 2: {1,2,3,4}, 3: {1,2,3,4}},
    3: {0: {1,2}, 1: {1,2,3}, 2: {1,2,3,4}, 3: {1,2,3,4}},
    4: {0: {1}, 1: {2}, 2: {3}, 3: {4}},
    0: {0: {1,2,3,4}, 1: {1,2,3,4}, 2: {1,2,3,4}, 3: {1,2,3,4}}
}

GRID = [[set(range(1,N+1)) for i in range(N)] for j in range(N)]
    
def solve_puzzle(clues):
    global GRID
    # SIMPLIFY as much as I can before bruteforce
    # all clues are going clockwise
    h_top_clues = clues[:4]
    v_left_clues = clues[4:8]
    h_bot_clues = clues[8:12]
    v_right_clues = clues[12:]
    # checking possibilities for cells values with clues
    for i in range(N):
        for j in range(N):
            GRID[j][i] = GRID[j][i].intersection(POSSIBILITIES[h_top_clues[i]][j])
            GRID[j][i] = GRID[j][i].intersection(POSSIBILITIES[h_bot_clues[N-i-1]][N-j-1])
            GRID[i][j] = GRID[i][j].intersection(POSSIBILITIES[v_right_clues[N-i-1]][j])
            GRID[i][j] = GRID[i][j].intersection(POSSIBILITIES[v_left_clues[i]][N-j-1])
    simplify = True
    while simplify:
        changes = False
        for i in range(N):
            for j in range(N):
                for el in GRID[i][j]:
                    if alone_in_cross((i, j), el):
                        changes = delete_from_cross((i,j), el)
                        GRID[i][j] = GRID[i][j].intersection((el,))
        simplify = True if changes else False
    # BRUTEFORCE
    puzzle = [[next(iter(el)) if len(el) == 1 else 0 for el in line] for line in GRID]
    unknown = [(row, col) for row in range(N) for col in range(N) if puzzle[row][col] == 0]
    curr_index = 0
    while 0 <= curr_index < len(unknown):
        #for line in puzzle:
        #    print(line)
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
        elif is_valid(puzzle, (curr_pos[0],curr_pos[1]),
                      (h_top_clues, v_left_clues, h_bot_clues, v_right_clues)):
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

def is_valid(grid, pos, clues):
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
    # check top horizontal clues
    prev_max = 0
    count = 0
    zero = False
    for i in range(N):
        if grid[i][pos[1]] == 0:
            zero = True
        if grid[i][pos[1]] > prev_max:
            count += 1
            prev_max = grid[i][pos[1]]
    clue = clues[0][pos[1]]
    if not zero and clue != 0 and count > clue:
        return False
    # check right vertical clues
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
    clue = clues[1][pos[0]]
    if not zero and clue != 0 and count > clue:
        return False
    # check bot horizontal clues
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
    clue = list(reversed(clues[2]))[pos[1]]
    if not zero and clue != 0 and count > clue:
        return False
    # check left vertical clues
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
    clue = list(reversed(clues[3]))[pos[0]]
    if not zero and clue != 0 and count > clue:
        return False
    return True
    
    
def alone_in_cross(pos, el):
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
                GRID[pos[0]][i] = GRID[pos[0]][i].difference((el,))
                deleted = True
        if i != pos[0]:
            if el in GRID[i][pos[1]]:
                GRID[i][pos[1]] = GRID[i][pos[1]].difference((el,))
                deleted = True
    return deleted
    