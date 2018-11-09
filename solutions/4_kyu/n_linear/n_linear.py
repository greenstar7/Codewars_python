"""Hrynevych Artemii
My solution for 4 kyu 'N Linear' kata
https://www.codewars.com/kata/n-linear
The kata wasn't available to test in python.
So i've left some easy tests.
"""

def n_linear(m, n):
    u = [1]
    # индексы елементов на которые мы умножамем М со списка
    indexes = [0 for _ in m]
    values = [None for _ in m]
    len_m = len(m)
    for i in range(n):
        for k in range(len_m):
            values[k] = m[k]*u[indexes[k]]+1
        min_val = min(values)
        u.append(min_val)
        for k in range(len_m):
            if values[k] == min_val:
                indexes[k] += 1
    return u[-1]

if __name__=='__main__':
    # U(5, 7, 8) = [1, 6, 8, 9, 31, 41, 43, 46, 49, 57, 64, 65, 73, 156, 206, ...]
    # U(2, 3) = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
    print(n_linear((5, 7, 8), 10))