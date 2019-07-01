""" Artemii Hrynevych
 tests for 4 Kyu kata 'Next smaller number with the same digits.

"""
import pytest

from next_smaller import next_smaller


class TestSolution:

    def test_correct_input(self):
        assert next_smaller(21) == 12
        assert next_smaller(531) == 513
        assert next_smaller(2071) == 2017
        assert next_smaller(998) == 989
        assert next_smaller(1234567908) == 1234567890


    def test_incorrect_input(self):
        assert next_smaller(9) == -1
        assert next_smaller(135) == -1
        assert next_smaller(1027) == -1
        assert next_smaller(123456789) == -1

