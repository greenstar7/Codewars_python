"""Hrynevych Artemii
My solution for "Memorized Fibonacci" kata
https://www.codewars.com/kata/529adbf7533b761c560004e5
"""

def fibonacci(n, cache={0: 0, 1: 1}):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]
