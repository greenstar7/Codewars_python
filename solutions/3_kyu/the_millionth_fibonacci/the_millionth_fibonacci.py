"""Hrynevych Artemii
My solution for 3 kyu 'The Millionth Fibonacci Kata'
https://www.codewars.com/kata/the-millionth-fibonacci-kata/python
"""

def fib(n):
    """Function to calculate n-th Fibonacci number as described in Exercise 1.19
    https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_thm_1.19
    """
    i = 1 if n>0 else (-1)**(n%2+1)
    return i*fib_iter(1, 0, 0, 1, i*n) 

def fib_iter(a, b, p, q, n):
    if n == 0:
        return b
    if n % 2 == 0:
        return fib_iter(a, b,
                        (q*q)+(p*p),
                        (2*p*q)+(q*q),
                        n//2)
    else:
        return fib_iter((b*q)+(a*q)+(a*p),
                        (b*p)+(a*q),
                        p, q, n-1)