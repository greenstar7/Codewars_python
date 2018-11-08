"""Hrynevych Artemii
My solution for 'Bit counting' kata
https://www.codewars.com/kata/526571aae218b8ee490006f4
"""

def countBits(n):
    """function to count how many 1`s will be in binary
    representation of given number(n)"""
    counter = 0
    while n > 0:
        counter = counter + n % 2
        n = n // 2
    return counter