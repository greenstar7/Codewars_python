import unittest
# from skyscrapers import solve_puzzle
from skyscrapers_constraints_propagation import solve_puzzle

class TestSkyscrapers(unittest.TestCase):
    def test_solutions(self):
        clues = ((3, 2, 2, 3, 2, 1,
                  1, 2, 3, 3, 2, 2,
                  5, 1, 2, 2, 4, 3,
                  3, 2, 1, 2, 2, 4),
                 
                 (0, 0, 0, 2, 2, 0,
                  0, 0, 0, 6, 3, 0,
                  0, 4, 0, 0, 0, 0,
                  4, 4, 0, 3, 0, 0))
        
        expected = ((( 2, 1, 4, 3, 5, 6 ),
                     ( 1, 6, 3, 2, 4, 5 ),
                     ( 4, 3, 6, 5, 1, 2 ),
                     ( 6, 5, 2, 1, 3, 4 ),
                     ( 5, 4, 1, 6, 2, 3 ),
                     ( 3, 2, 5, 4, 6, 1 )),
                    
                    (( 5, 6, 1, 4, 3, 2 ),
                     ( 4, 1, 3, 2, 6, 5 ), 
                     ( 2, 3, 6, 1, 5, 4 ), 
                     ( 6, 5, 4, 3, 2, 1 ), 
                     ( 1, 2, 5, 6, 4, 3 ), 
                     ( 3, 4, 2, 5, 1, 6 )))
        
        for i in range(len(clues)):
            with self.subTest(i=i):
                self.assertEqual(expected[i], solve_puzzle(clues[i]))
            
if __name__ == '__main__':
    unittest.main()    