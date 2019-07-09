""" Hrynevych Artemii
Tests for my solutions for 4 kyu 'Infix to postfix converter' kata.

"""
from infix_to_postfix import to_postfix, _split_to_list


def test_split_to_list():
    cases = {
        '3*3/(7+1)': ['3', '*', '3', '/', '(7+1)'],
        '7+1': ['7', '+', '1'],
        '3': ['3']
    }
    for input_str, true_res in cases.items():
        assert true_res == _split_to_list(input_str)


def test_to_postfix():
    cases = {
        '2+7*5': '275*+',
        '3*3/(7+1)': '33*71+/',
        '5+(6-2)*9+3^(7-1)': '562-9*+371-^+',
        '(5-4-1)+9/5/2-7/1/7")': '54-1-95/2/+71/7/-'
    }
    for input_str, true_res in cases.items():
        assert true_res == to_postfix(input_str)
