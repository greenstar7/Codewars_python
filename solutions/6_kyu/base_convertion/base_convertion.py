"""Hrynevych Artemii
My solution for the Codewars "Base conversion" kata
https://www.codewars.com/kata/base-conversion
"""

def convert(input_num, source, target):
    """Function to convert input number 
    from source base to target base
    
    Arguments:
    input_num -- input number to convert
    source -- source base of the number
    target -- target base to convert the number
    """
    source_base = len(source)
    i = 0
    in_dec = 0
    # from source to decimal
    for char in input_num[::-1]:
        in_dec = in_dec + (source_base**i)*source.index(char)
        i+=1
    # from decimal to target base
    target_base = len(target)
    # if we have 0 from the start we will never enter "while"
    # so we need to take it into account
    res = '' if in_dec != 0 else target[0]
    while in_dec != 0:
        res = target[in_dec%target_base] + res
        in_dec = in_dec // target_base
    return res