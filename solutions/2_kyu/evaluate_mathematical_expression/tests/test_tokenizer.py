""" Hrynevych Artemii 2019
Tokenizer tests.

"""
from eval_math_expr import TokenType, Token, Tokenizer
import pytest


def test_tokenizer():
    """ Test case with multiple whitespaces, parenthesis, all operators

    """
    correct_string = '((12 +    -3) * 100 / +2)   '
    answers = [
        Token(tvalue='(', ttype=TokenType.lpar),
        Token(tvalue='(', ttype=TokenType.lpar),
        Token(tvalue='12', ttype=TokenType.number),
        Token(tvalue='+', ttype=TokenType.plus),
        Token(tvalue='-', ttype=TokenType.minus),
        Token(tvalue='3', ttype=TokenType.number),
        Token(tvalue=')', ttype=TokenType.rpar),
        Token(tvalue='*', ttype=TokenType.mul),
        Token(tvalue='100', ttype=TokenType.number),
        Token(tvalue='/', ttype=TokenType.div),
        Token(tvalue='+', ttype=TokenType.plus),
        Token(tvalue='2', ttype=TokenType.number),
        Token(tvalue=')', ttype=TokenType.rpar)]
    tokenizer = Tokenizer(correct_string)
    for true_token in answers:
        ret_token = tokenizer.get_next_token()
        assert ret_token == true_token
