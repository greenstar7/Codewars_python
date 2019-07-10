""" Artemii Hrynevych - solution for 3 kyu 'Huffman encoding' kata.

"""
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Tuple

FrequencyCount = Tuple[str, int]
FrequencyCounts = List[FrequencyCount]


@dataclass(frozen=True)
class HuffmanTree:
    """ Simple implementation of binary tree for Huffman encoding.

    Attributes
    ----------
    weight : int
        Occurrences number of char or (if char is empty) sum of weights
        from trees below.
    text : str
        Has all chars form nodes below if node is not leaf.
        For leafs it is the character the leaf represents.
    right : HuffmanTree
        Right subtree.
    left : HuffmanTree
        Left subtree.

    """
    weight: int
    text: str = ''
    left: 'HuffmanTree' = None
    right: 'HuffmanTree' = None

    def encode(self, text: str) -> str:
        """ Encodes text with the huffman encoding.

        Parameters
        ----------
        test : str
            Input text which will be encoded.

        Returns
        -------
        None
            If there are one or less characters in the text.
        encoded_text : str
            Text coded with Huffman encoding.

        """
        cache = dict()
        encoded_text = ''
        for char in text:
            try:
                encoded_text += cache[char]
            except KeyError:
                encoded_text += self.get_char_code(char)
        return encoded_text

    def get_char_code(self, char: str) -> str:
        """ Encodes one single character with the huffman encoding.

        Parameters
        ----------
        char : str
            Single character which will be searched for in the tree.

        Returns
        -------
        code : str
            Encoded charater. Is empty if char is not in the tree.

        """
        code = ''
        curr = self
        while curr != None and char != curr.text:
            if char in curr.left.text:
                curr = curr.left
                code += '0'
            elif char in curr.right.text:
                curr = curr.right
                code += '1'
        return code

    def decode(self, text: str) -> str:
        """ Decodes given encoded text with the huffman encoding.

        Parameters
        ----------
        text : str
            Encoded text which will be decoded.

        Returns
        -------
        decoded_text : str
            Text decoded with Huffman encoding.

        """
        decoded_text = ''
        curr = self
        for char in text:
            if char == '0':
                curr = curr.left
            elif char == '1':
                curr = curr.right

            if curr.left is None and curr.right is None:
                decoded_text += curr.text
                curr = self

        return decoded_text


def frequencies(text: str) -> FrequencyCounts:
    """ Function to get frequencies of characters in the string.

    Parameters
    ----------
    text : str
        Original text as unicode string.

    Returns
    -------
    None
        If string is empty or has only 1 character.
    counts: list of (char, int) tuples
        Character counts.

    """
    counts = defaultdict(int)
    for char in text:
        counts[char] += 1
    return list(counts.items())


def build_tree(fs: FrequencyCounts) -> HuffmanTree:
    """ Function to built Huffman tree from the given char frequencies.

    Parameters
    ----------
    fs : FrequencyCounts
        Character counts, from which HuffmanTree will be built.

    Returns
    -------
    HuffmanTree
        Which was built from the given frequencies.

    """
    fs = sorted(fs, key=lambda x: x[1])
    trees = []
    for char, count in fs:
        trees.append(HuffmanTree(weight=count, text=char))
    while len(trees) > 1:
        trees = sorted(trees, key=lambda x: x.weight, reverse=True)
        right = trees.pop()
        left = trees.pop()
        summed_weight = right.weight + left.weight
        text = ''.join(sorted(right.text + left.text))
        trees.append(
            HuffmanTree(weight=summed_weight, text=text, right=right, left=left))
    return trees.pop()


def encode(fs: FrequencyCounts, text: str) -> str:
    """ Encodes text with the huffman encoding.

    Parameters
    ----------
    fs : FrequencyCount or list of (str, int) tuples
        List of (char, number of occurrence of this char) tuples
    test : str
        Input text which will be encoded.

    Returns
    -------
    None
        If there are no characters in the text.
    encoded_text : str
        Text coded with Huffman encoding.

    """
    if len(fs) <= 1:
        return None
    tree = build_tree(fs)
    encoded_text = tree.encode(text)
    return encoded_text


def decode(fs: FrequencyCounts, encoded_text: str) -> str:
    """ Decodes given encoded text with the huffman encoding.

    Parameters
    ----------
    fs : FrequencyCount or list of (str, int) tuples
        List of (char, number of occurrence of this char) tuples,
        from which Huffman tree will be built.
    encoded_text : str
        Encoded text which will be decoded.

    Returns
    -------
    None
        If there are no characters in the encoded_text or in the fs.
    decoded_text : str
        Text decoded with Huffman encoding.

    """
    if len(fs) <= 1:
        return None
    tree = build_tree(fs)
    decoded_text = tree.decode(encoded_text)
    return decoded_text
