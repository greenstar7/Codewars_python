""" Artemii Hrynevych
 tests for 4 Kyu kata 'Next smaller number with the same digits.

"""
import pytest

from next_bigger import next_bigger


class TestSolution:

    def test_correct_input(self):
        assert next_bigger(12) == 21
        assert next_bigger(513) == 531
        assert next_bigger(2017) == 2071
        assert next_bigger(989) == 998
        assert next_bigger(1234567890) == 1234567908


    def test_incorrect_input(self):
        assert next_bigger(9) == -1
        assert next_bigger(987) == -1
        assert next_bigger(72) == -1

