"""Hrynevych Artemii
My solution for Codewars "The observed PIN" kata
https://www.codewars.com/kata/the-observed-pin
"""
#┌───┬───┬───┐
#│ 1 │ 2 │ 3 │
#├───┼───┼───┤
#│ 4 │ 5 │ 6 │
#├───┼───┼───┤
#│ 7 │ 8 │ 9 │
#└───┼───┼───┘
#    │ 0 │
#    └───┘

# all possibilities of mistakes
# f.e. 1 could have been mistaken with 2 and 4 
# or just it may be correct
POSSIBILITIES = {'1':'124','2':'1235', '3':'236',
                 '4':'1457','5':'24568','6':'3569',
                 '7':'478','8':'57890','9':'689',
                 '0':'80'}

def get_pins(observed_pin):
    """ Function to get all possible variants of observed pin"""
    result = ['']
    for char in observed_pin:
        result = [ previous_combination + possibility 
                  for previous_combination in result 
                  for possibility in POSSIBILITIES[char] ]
    return result