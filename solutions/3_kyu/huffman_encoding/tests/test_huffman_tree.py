""" Tests for Huffman tree and related functions. """
from huffman_encoding import HuffmanTree, build_tree, encode, frequencies
import pytest


@pytest.fixture(scope='module')
def tree():
    tree = HuffmanTree(
        weight=19, text='abcq',
        left=HuffmanTree(
            weight=10, text='q', left=None, right=None),
        right=HuffmanTree(
            weight=9, text='abc',
            left=HuffmanTree(
                weight=5, text='ab',
                left=HuffmanTree(
                    weight=3, text='a', left=None, right=None),
                right=HuffmanTree(
                    weight=2, text='b', left=None, right=None)),
            right=HuffmanTree(weight=4, text='c', left=None, right=None)))
    return tree


class TestHuffmanTree:

    def test_build_tree(self, tree):
        func_input = frequencies('aaabbccccqqqqqqqqqq')
        assert tree == build_tree(func_input)

    def test_get_char_code(self, tree):
        cases = {
            'a': '100',
            'b': '101',
            'c': '11',
            'q': '0',
        }
        for char, true_code in cases.items():
            assert true_code == tree.get_char_code(char)

    def test_encode(self, tree):
        cases = {
            'aaabbccccqqqqqqqqqq':  3*3 + 3*2 + 4*2 + 10*1,
            'qqc': 2*1 + 1*2,
            '': 0
        }
        for text, len_encoded in cases.items():
            encoded_text = tree.encode(text)
            assert len(encoded_text) == len_encoded

    def test_decode(self, tree):
        cases = {
            '101': 'b',
            '100100': 'aa',
            '101100101100': 'baba',
            '001000100101': 'qqaqab',
            '': ''
        }
        for text, true_res in cases.items():
            assert true_res == tree.decode(text)
