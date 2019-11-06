""" Hrynevych Artemii
My solution for 3 kyu 'Calculator' kata.
https://www.codewars.com/kata/calculator

"""
from enum import IntEnum


class TokenType(IntEnum):
    """ Enum to organize token types. 
    
    """
    lpar = 0
    rpar = 1
    plus = 2
    minus = 3
    mul = 4
    div = 5
    number = 6


class Token:
    """ Simple token class. 
    
    """
    
    def __init__(self, tvalue, ttype) -> None:
        self.tvalue = tvalue
        self.ttype = ttype


class Tokenizer:
    """ Tokenizer class to split input expression into tokens.

    """

    def __init__(self, input_string: str) -> None:
        self.string = input_string
        print('self.string', self.string)
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

    def _get_number_string(self):
        number_string = ''
        while self.string[self.idx].isdigit():
            number_string += self.string[self.idx]
            self.idx += 1
            if self.idx >= self.N:
                break
        return number_string

    def _get_number_token(self):
        number_string = self._get_number_string()
        if self.idx < self.N and self.string[self.idx] == '.':
            self.idx += 1
            number_string += '.' + self._get_number_string()
        return Token(tvalue=number_string, ttype=TokenType.number)


class Calculator:
    """ Simple Calculator implementation.
    
    """

    def __init__(self) -> None:
        pass

    def evaluate(self, expression_str: str = None) -> float:
        self._tokens = []
        self.tokenizer = Tokenizer(expression_str)
        return self._expr()

    def _expr(self) -> float:
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

    def _term(self) -> float:
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

    def _factor(self) -> float:
        self._get_next_token()
        if self.curr_token.ttype == TokenType.plus:
            return self._factor()
        elif self.curr_token.ttype == TokenType.minus:
            return - self._factor()
        elif self.curr_token.ttype == TokenType.number:
            return float(self.curr_token.tvalue)
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

