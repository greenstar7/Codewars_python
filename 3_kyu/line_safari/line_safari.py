def show_grid(grid):
    ''' Function to show 2d matrix representing the grid for our line'''
    for line in grid:
        print(line)

def line(grid):
    ''' Function to check if the grid has a valid line'''
    start_points = get_start_points(grid)
    for point in start_points:
        print(f'checking {point}')
        if check_line(grid, point):
            return True
    return False

def get_start_points(grid, start='X'):
    ''' Function to get the coordinates of the start points'''
    rows = range(len(grid))
    cols = range(len(grid[0]))
    # returning the list of positions of start points
    return [(r,c) for r in rows for c in cols if grid[r][c] == start]

def check_line(grid, start):
    ''' Function to check whether there is a line from this starting point
    to another one'''
    prev = None
    curr = start
    path = [ [' ' for char in line] for line in grid]
    path[curr[0]][curr[1]] = grid[curr[0]][curr[1]]
    # find next step
    next = get_first_next(grid, curr)
    # while next step is valid
    while next is not None:
        prev = curr
        curr = next
        path[curr[0]][curr[1]] = grid[curr[0]][curr[1]]
        # until you find the exit
        if grid[curr[0]][curr[1]] == 'X':
            path = [''.join(line) for line in path]
            if grid == path:
                return True
            else:
                return False
        else:
            # continue to go further
            next = get_next(grid, prev, curr)
        print(prev, curr, next)
    # if next step is not valid
    return False
        
def get_first_next(grid, curr):
    ''' Function to find the first neighbour of the start cell
    to continue goint through the line'''
    rows = len(grid)
    cols = len(grid[0])
    first_next = None
    print(f'getting first heighbour')
    # checking the left neighbour
    if 0 <= curr[1]-1:
        temp = grid[curr[0]][curr[1]-1]
        if temp in '-+X':
             first_next = (curr[0],curr[1]-1)
    # checking the right neighbour
    if curr[1]+1 < cols:
        temp = grid[curr[0]][curr[1]+1]
        if temp in '-+X':
            if first_next:
                return None
            else:
                first_next = (curr[0],curr[1]+1)
    # checking the top neighbour
    if curr[0]-1 >= 0:
        temp = grid[curr[0]-1][curr[1]]
        if temp in '|+X':
            if first_next:
                return None
            else:
                first_next = (curr[0]-1,curr[1])
    # checking the bot neighbour
    if curr[0]+1 < rows:
        temp = grid[curr[0]+1][curr[1]]
        if temp in '|+X':
            if first_next:
                return None
            else:
                first_next = (curr[0]+1,curr[1])
    return first_next
        
def get_next(grid, prev, curr):
    ''' Function to get the position of the next cell
    or None if there is no right place to go'''
    print(f'getting next')
    rows = len(grid)
    cols = len(grid[0])
    drctn = (curr[0]-prev[0], curr[1]-prev[1])
    curr_type = grid[curr[0]][curr[1]]
    if curr_type in '-|X':
        try:
            next = (curr[0]+drctn[0], curr[1]+drctn[1])
            next_type = grid[next[0]][next[1]]
        except IndexError:
            return None
        else:
            if curr_type == next_type or next_type in '+X':
                return next
            else:
                return None
    elif curr_type == '+':
        # DOESNT WORK PROPERLY
        # TODO
        in_direction = (curr[0]+drctn[0], curr[1]+drctn[1])
        PERPENDICULAR = {(1, 0): ' -', (-1, 0): ' -', (0, 1): ' |', (0, -1): ' |'}
        IN_DIR_TYPE = {(1, 0): '|', (-1, 0): '|', (0, 1): '-', (0, -1): '-'}
        # if there is something in direction of movement
        if 0 <= in_direction[0] < rows and 0 <= in_direction[1] < cols:
            in_dir_type = grid[in_direction[0]][in_direction[1]]
            if in_dir_type in IN_DIR_TYPE[drctn[0], drctn[1]]:
                # that means it's not a corner
                return None
        right_side = (curr[0]-drctn[1], curr[1]-drctn[0])
        if 0 <= right_side[0] < rows and 0 <= right_side[1] < cols:
            right_side_type = grid[right_side[0]][right_side[1]]
            #if right_side_type == IN_DIR_TYPE[(-drctn[1],-drctn[0])] or right_side_type == '+':   
            #    return right_side
            if right_side_type in PERPENDICULAR[(-drctn[1],-drctn[0])]:
                right_side = None
            print(f'right side {right_side_type}')
        else:
            right_side = None
        left_side = (curr[0]+drctn[1], curr[1]+drctn[0])
        if 0 <= left_side[0] < rows and 0 <= left_side[1] < cols:
            left_side_type = grid[left_side[0]][left_side[1]]
            #if left_side_type == IN_DIR_TYPE[(drctn[1],drctn[0])] or left_side_type == '+':
            #    return left_side
            if left_side_type in PERPENDICULAR[(drctn[1],drctn[0])]:
                left_side = None
            print(f'left side {left_side_type}')
        else:
            left_side = None
        if right_side and left_side:
            return None
        else:
            return right_side or left_side
    return None

# my little test
if __name__=='__main__':
    grids = [    ['    ',
                  'X   ',
                  'X   '
                  '    '],
                 [' X  ',
                  ' X  '
                  '    '],
                 ["           ",
                  "X---------X",
                  "           ",
                  "           "],
                 ["     ",
                  "  X  ",
                  "  |  ",
                  "  |  ",
                  "  X  "],
                 ['+-----+',  
                  '|     |',
                  'X     X',
                  '|     |',
                  '+-----+'],
                 [ '    +----+  ',
                   '    |+--+|  ',
                   '    ||X+||  ',
                   '    |+-+||  ',
                   '    +---+|  ',
                   'X--------+  '],
                 ["                    ",
                  "     +--------+     ",
                  "  X--+        +--+  ",
                  "                 |  ",
                  "                 X  ",
                  "                    "],
                 ["                     ",
                  "    +-------------+  ",
                  "    |             |  ",
                  " X--+      X------+  ",
                  "                     "],
                 ["                      ",
                  "   +-------+          ",
                  "   |      +++---+     ",
                  "X--+      +-+   X     "],
                 ["      +------+",
                  "      |      |",
                  "X-----+------+",
                  "      |       ",
                  "      X       "],
                ['   X     X   ',
                 '   ++++  +-+ ',
                 '    +++--+ | ',
                 '         +-+ ']]
    for grid in grids:
        show_grid(grid) # just want to see the grid before we start
        print(get_start_points(grid))
        print(f'{"-"*86}\nRESULT{"-"*80}>>>>>> {line(grid)}')