"""Hrynevych Artemii
My solution for 4 kyu 'Twice linear' kata
https://www.codewars.com/kata/twice-linear
"""

def dbl_linear(n):
    u = [1]
    left = 0
    right = 0
    for i in range(n):
        left_val = 2*u[left] + 1
        right_val = 3*u[right] + 1
        if left_val <= right_val:
            u.append(left_val)
            left += 1
            if left_val == right_val:
                right += 1
        else:
            u.append(right_val)
            right += 1
    return u[-1]