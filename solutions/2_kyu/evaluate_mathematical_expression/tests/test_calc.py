""" Hrynevych Artemii
Tests for 'Evaluate mathematical expression' kata.

"""
from eval_math_expr import calc


def test_calc():
    tests = [
        ["1 + 1", 2],
        ["8/16", 0.5],
        ["3 -(-1)", 4],
        ["2 + -2", 0],
        ["10- 2- -5", 13],
        ["(((10)))", 10],
        ["3 * 5", 15],
        ["-7 * -(6 / 3)", 14]]
    for test in tests:
        assert calc(test[0]) == test[1]
