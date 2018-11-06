import unittest
from skyscrapers import solve_puzzle

class TestSkyscrapers(unittest.TestCase):
    def test_solutions(self):
        clues = (
                ( 2, 2, 1, 3,  
                  2, 2, 3, 1,  
                  1, 2, 2, 3,  
                  3, 2, 1, 3 ),
                ( 0, 0, 1, 2,   
                  0, 2, 0, 0,   
                  0, 3, 0, 0, 
                  0, 1, 0, 0 )
                )
        outcomes = (
                    ( ( 1, 3, 4, 2 ),       
                      ( 4, 2, 1, 3 ),       
                      ( 3, 4, 2, 1 ),
                      ( 2, 1, 3, 4 ) ),
                    ( ( 2, 1, 4, 3 ), 
                      ( 3, 4, 1, 2 ), 
                      ( 4, 2, 3, 1 ), 
                      ( 1, 3, 2, 4 ) )
                    )
        for i in range(len(clues)):
            with self.subTest(i=i):
                self.assertEqual(outcomes[i], solve_puzzle(clues[i]))
            
if __name__ == '__main__':
    unittest.main()