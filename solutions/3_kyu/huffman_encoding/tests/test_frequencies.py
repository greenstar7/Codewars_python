""" Artemii Hrynevych - tests for my solution for 'Huffman encoding' kata.

"""
from huffman_encoding import frequencies


def test_frequencies():
    cases = {
        'aabbccsda': [('a', 3), ('b', 2), ('c', 2), ('d', 1), ('s', 1)],
        'AAaaqqqq': [('A', 2), ('a', 2), ('q', 4)],
        'aaaaaa': [('a', 6)],
        '': []
    }
    for test_string, true_res in cases.items():
        assert true_res == sorted(frequencies(test_string))
