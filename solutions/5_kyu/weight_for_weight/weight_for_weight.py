"""Hrynevych Artemii
My solution for 5 kyu 'Weight for weight' kata
https://www.codewars.com/kata/weight-for-weight
"""

def order_weight(strng):
    # sort nums as so that when we will sort by weights
    # the nums will be already sorted in the result as strings
    strng = sorted(strng.strip().split())
    # sort nums by their wight (sum of digits)
    res = sorted(strng, key=lambda x: sum([int(digit) for digit in x]))
    # returning result as one string
    return ' '.join(res)