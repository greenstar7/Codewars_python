''' Hrynevych Artemii
My solution for the Codewars "Exes and oxes" kata
https://www.codewars.com/kata/55908aad6620c066bc00002a'''

def xo(string):
    """Function that checks if the number of o's
    is equal to the number of x's in the string"""
    o_counter = 0
    x_counter = 0
    for char in string.lower():
        if char == 'x':
            x_counter += 1
        elif char == 'o':
            o_counter += 1
    return x_counter == o_counter