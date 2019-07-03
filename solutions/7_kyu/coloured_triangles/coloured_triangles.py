""" Hrynevych Artemii
My solution for 7 Kyu 'Coloured Triangles' kata

"""


def double(row): 
    if len(row) == 1:
        return row
    elif row[0] == row[1]:
        return row[0]
    elif 'B' in row:
        if 'R' in row: # BR or RB
            return 'G'
        elif 'G' in row: # BG or GB
            return 'R'
    elif 'R' in row:
        if 'G' in row: # RG or GR
            return 'B'


def triangle(row: str) -> str:
    while len(row) != 1:
        temp = ''
        for i in range(0, len(row)-1):
            temp += double(row[i: i+2])
            print('temp', temp)
        row = temp
    return row

