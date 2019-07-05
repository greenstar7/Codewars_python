""" Hrynevych Artemii 2019
Tokenizer tests.

"""
from eval_math_expr import TokenType, Token, Tokenizer
import pytest


class TestTokenizer:

    def test_correct_example(self):
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
        for ret_token, true_token in zip(tokenizer, answers):
            assert ret_token == true_token

    def test_wrong_example(self):
        """ Test case with wrong symbol in expression.

        """
        wrong_string = '(2 + 3) ~ 4'
        tokenizer = Tokenizer(wrong_string)
        with pytest.raises(RuntimeError):
            list(tokenizer)
