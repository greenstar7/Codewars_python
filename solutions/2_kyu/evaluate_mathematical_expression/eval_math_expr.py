""" Hrynevych Artemii
My solution for 2 kyu 'Evaluate mathematical expression' kata.

"""
from enum import Enum
from typing import Iterator, NamedTuple


class TokenType(Enum):
    """ Enum to organize token types. """
    lpar = 0
    rpar = 1
    plus = 2
    minus = 3
    mul = 4
    div = 5
    number = 6


class Token(NamedTuple):
    """ Simple token class as a named tuple. """
    tvalue: str
    ttype: TokenType


class Tokenizer:
    """ Tokenizer class to split input expression into tokens.

    """

    def __init__(self, input_string: str) -> None:
        self.string = input_string
        self.N = len(self.string)
        self.idx = 0

    def get_next_token(self) -> Token:
        if self.idx >= self.N:
            raise StopIteration
        if self.string[self.idx].isspace():
            while self.string[self.idx].isspace():
                self.idx += 1
                if self.idx >= self.N:
                    raise StopIteration
        char = self.string[self.idx]
        if char.isdigit():
            return self._get_number_token()
        else:
            if char == '(':
                token_type = TokenType.lpar
            elif char == ')':
                token_type = TokenType.rpar
            elif char == '+':
                token_type = TokenType.plus
            elif char == '-':
                token_type = TokenType.minus
            elif char == '/':
                token_type = TokenType.div
            elif char == '*':
                token_type = TokenType.mul
            self.idx += 1
            return Token(tvalue=char, ttype=token_type)

    def _get_number_token(self):
        number_string = ''
        while self.string[self.idx].isdigit():
            number_string += self.string[self.idx]
            self.idx += 1
            if self.idx >= self.N:
                break
        return Token(tvalue=number_string, ttype=TokenType.number)


class Expression:

    def __init__(self, expression_str: str) -> None:
        self.expression_str = expression_str
        self.tokenizer = Tokenizer(expression_str)
        self._tokens = []

    def evaluate(self) -> int:
        return self._expr()

    def _expr(self) -> int:
        print('\texpr')
        ret_val = self._term()
        while True:
            self._get_next_token()
            if self.curr_token is None:
                break
            elif self.curr_token.ttype == TokenType.plus:
                next_term = self._term()
                ret_val = ret_val + next_term
            elif self.curr_token.ttype == TokenType.minus:
                next_term = self._term()
                ret_val = ret_val - next_term
            else:
                self._push_token_back()
                break
        return ret_val

    def _term(self) -> int:
        print('\tterm')
        ret_val = self._factor()
        while True:
            self._get_next_token()
            if self.curr_token is None:
                break
            elif self.curr_token.ttype == TokenType.mul:
                next_factor = self._factor()
                ret_val = ret_val * next_factor
            elif self.curr_token.ttype == TokenType.div:
                next_factor = self._factor()
                ret_val = ret_val / next_factor
            else:
                self._push_token_back()
                break
        return ret_val

    def _factor(self) -> int:
        print('\tfactor')
        self._get_next_token()
        if self.curr_token.ttype == TokenType.plus:
            return self._factor()
        elif self.curr_token.ttype == TokenType.minus:
            print('\tunary minus')
            return - self._factor()
        elif self.curr_token.ttype == TokenType.number:
            print('\number')
            return int(self.curr_token.tvalue)
        elif self.curr_token.ttype == TokenType.lpar:
            expr_res = self._expr()
            self._get_next_token()
            return expr_res
        else:
            self._push_token_back()

    def _push_token_back(self) -> None:
        self._tokens.append(self.curr_token)

    def _get_next_token(self) -> None:
        if self._tokens:
            self.curr_token = self._tokens.pop()
        else:
            try:
                self.curr_token = self.tokenizer.get_next_token()
            except StopIteration:
                self.curr_token = None
        print('TOKEN:', self.curr_token)


def calc(expression_str: str) -> int:
    expression = Expression(expression_str)
    return expression.evaluate()
