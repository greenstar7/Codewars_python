"""Artemii Hrynevych
My solution for 6 kyu "Array.diff" kata
https://www.codewars.com/kata/array-dot-diff/
"""

def array_diff(a, b):
    """Function to substract list b from list a.
    Returns the difference as a list."""
    return [el for el in a if el not in b] # pythonic way
    # but if you want to make it complex
    # and without list comprehensions
    # b_i = 0
    # a_i = 0
    # a_n = len(a)
    # b_n = len(b)
    # res = []
    # while a_i < a_n:
    #     b_i = 0
    #     while b_i < b_n:
    #         if a[a_i] == b[b_i]:
    #             a_i += 1
    #             break
    #         else:
    #             b_i += 1
    #     if b_i == b_n:
    #         res.append(a[a_i])
    #         a_i += 1
    # return res