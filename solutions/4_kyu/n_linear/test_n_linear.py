"""Hrynevych Artemii
Simple test for my 'N Linear' kata solution
"""

import unittest
from n_linear import n_linear

class TestNLinear(unittest.TestCase):
    def test_answers(self):
        m = ((5,7,8), (2, 3))
        sequences = [
            [1, 6, 8, 9, 31, 41, 43, 46, 49, 57, 64, 65, 73, 156, 206],
            [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27]
        ]
        for i in range(len(m)):
            for n in range(1, len(sequences[i])):
                with self.subTest(m=m[i], seq=sequences[i], n=n):
                    self.assertEqual(n_linear(m[i], n), sequences[i][n])
            
if __name__ == '__main__':
    unittest.main()