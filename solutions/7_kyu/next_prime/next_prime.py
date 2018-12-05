"""Hrynevych Artemii
My solution for 7 kyu 'Next Prime' kata
https://www.codewars.com/kata/next-prime/python"""

def primes(up_to):
    nums = [False, False] + [True for _ in range(up_to)]
    for i in range(2, up_to):
        if nums[i] is True:
            for j in range(i*2, up_to, i):
                nums[j] = False
    return [i for i in range(up_to) if nums[i] is True]  
    
def is_prime(num):
    for prime in primes(int(num**0.5)+1):
        if num%prime==0:
            return False
    return True

def next_prime(n):
    if n == 0: return 2
    next = n+1
    while not is_prime(next):
        next += 1
    return next