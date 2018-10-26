''' Hrynevych Artemii
My solution for the Codewars "Line Safari" kata
https://www.codewars.com/kata/line-safari-is-that-a-line/python'''

def line(grid):
    ''' Function to check if the grid has a valid line'''
    start_points = get_start_points(grid)
    # just finding dimensions of the array to calculate it only once
    rows = len(grid)
    cols = len(grid[0])
    for point in start_points:
        if check_line(grid, point, rows, cols):
            return True
    return False

def get_start_points(grid, start='X'):
    ''' Function to get the coordinates of the start points'''
    rows = range(len(grid))
    cols = range(len(grid[0]))
    # returning the list of positions of start points
    return [(r,c) for r in rows for c in cols if grid[r][c] == start]

def check_line(grid, start, rows, cols):
    ''' Function to check whether there is a line from this starting point
    to another one'''
    curr = start
    # creating new array for the path we walked
    path = [ [char for char in line] for line in grid]
    # and writing cells we walked through to it
    path[curr[0]][curr[1]] = ' '
    # find next step
    next = get_first_next(grid, curr, rows, cols)
    # while next step is valid
    while next is not None:
        dir_vec = (next[0]-curr[0], next[1]-curr[1])
        path[curr[0]][curr[1]] = ' '
        curr = next
        # until you find the exit
        if grid[curr[0]][curr[1]] == 'X':
            path[curr[0]][curr[1]] = ' '
            if check_path_is_empty(path):
                return True
            else:
                return False
        else:
            # continue to go further
            next = get_next(path, dir_vec, curr, rows, cols)
    # if next step is not valid
    # and we didn't reach the end before
    return False
        
def get_first_next(grid, curr, rows, cols):
    ''' Function to find the first neighbour of the start cell
    to continue goint through the line'''
    first_next = None
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
        
def get_next(grid, dir_vec, curr, rows, cols):
    ''' Function to get the position of the next cell
    or None if there is no right place to go'''
    curr_type = grid[curr[0]][curr[1]]
    
    # next pos in direction of movement
    in_dir_pos = (curr[0] + dir_vec[0], curr[1] + dir_vec[1])
    # if next position in direction of mevement is in the list
    # and we can get it's value
    if 0 <= in_dir_pos[0] < rows and 0 <= in_dir_pos[1] < cols:
        in_dir_type = grid[in_dir_pos[0]][in_dir_pos[1]]
    else:
        in_dir_type = None
    # if the cell we are currently on is a '-' or '|'
    # the next one must be '+' or the same type to be valid
    if curr_type in '-|':
        if in_dir_type in ''.join(('+', 'X',curr_type)):
            return in_dir_pos
    # otherwise it must be a corner
    elif curr_type == '+':
        # '+' might be a corner if the next cell is perpendicular
        # for example '|' is we are going right/left
        # or next cell is none, whitespace or '+'
        perp = perpendicular[dir_vec]
        if in_dir_type in (None, '+', ' ', perp):
            # if this '+' may be a corner let's check right and left
            # for this '+' to be a corner it must have right or left neighbor
            # and only one neighbor
            # otherwise (2 neighbors or no neighbor) it's not a corner
            # neighbors must be perpendicular to direction vector or '+'
            right = (curr[0] - dir_vec[1], curr[1] - dir_vec[0])
            left = (curr[0] + dir_vec[1], curr[1] + dir_vec[0])
            if 0 <= right[0] < rows and 0 <= right[1] < cols:
                right_type = grid[right[0]][right[1]]
                if right_type not in ('+', perp, 'X'):
                    right_type = None 
            else:
                right_type = None
            if 0 <= left[0] < rows and 0 <= left[1] < cols:
                left_type = grid[left[0]][left[1]]
                if left_type not in ('+', perp, 'X'):
                    left_type = None 
            else:
                left_type = None
            if left_type and right_type:
                return None
            elif left_type:
                return left
            elif right_type:
                return right
    return None 
    
def check_path_is_empty(path):
    for line in path:
        for char in line:
            if char != ' ':
                return False
    return True
