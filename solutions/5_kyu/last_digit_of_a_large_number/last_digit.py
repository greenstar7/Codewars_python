""" Hrynevych Artemii
My solution for 5 Kyu 'Last digit of a large number' kata.

"""


def last_digit(n1, n2):
    n1 = n1%10
    n2 = bin(n2)[:1:-1]
    res = 1
    for char in n2:
        if char == '1':
            res *= n1
        n1 = (n1*n1) % 10
    
    return res % 10
