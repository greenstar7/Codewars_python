"""Hrynevych Artemii
My solution for 7 kyu 'Narcissistic Numbers' kata
https://www.codewars.com/kata/narcissistic-numbers/
"""

def is_narcissistic(num):
    n = 0
    digits = []
    temp = num
    while temp > 0:
        n += 1
        digits.append(temp%10)
        temp //= 10
    return sum(x**n for x in digits) == num