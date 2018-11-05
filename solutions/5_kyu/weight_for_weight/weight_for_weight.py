"""Hrynevych Artemii
My solution for 5 kyu 'Weight for weight' kata
https://www.codewars.com/kata/weight-for-weight
"""

def weight_weight(weight):
    return sum([int(digit) for digit in weight])

def order_weight(string):
    """Function to sort the string of numbers by it weights
    (sun of digits) and numbers with the same weight are sorted
    as strings.
    Arguments:
    string -- string of numbers to sort
    """
    weights = string.strip().split()
    weights_weights = [[weight_weight(weight), weight] for  weight in weights]
    # sorting by sum of digits
    sorted_w_w = sorted(weights_weights, key = lambda x: x[0])
    # sorting by strings comparison
    curr_w = -1
    temp = []
    res = ''
    for i in range(len(sorted_w_w)):
        if sorted_w_w[i][0] != curr_w:
            curr_w = sorted_w_w[i][0]
            if res:
                res = ' '.join((res, ' '.join(sorted(temp))))
            else:
                res = ' '.join(sorted(temp))
            temp = []
        temp.append(sorted_w_w[i][1])
    if temp:
        res = ' '.join((res, ' '.join(sorted(temp))))
    # joining the sorted list as string
    return res