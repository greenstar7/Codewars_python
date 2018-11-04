""" Hrynevych Artemii
My solution for the Codewars "5x5 Nonogram Solver" kata
https://www.codewars.com/kata/5x5-nonogram-solver/python
"""

BLANK = '.'
FILLED = '#'
BANNED = 'X'
    
class Nonogram:
    """ Implementation of 5x5 nonogram solver."""
    
    def __init__(self, clues):
        """ Writing downt the clues.
        
        Arguments:
        clues -- tuple of (horizontal clues, vertical clues).
        Horizontal and vertical clues are given as tuples of indiviadual clues.
        """
        self.__clues = clues
        self.__grid = [[BLANK for col in range(5)] for row in range(5)]

    def solve(self):
        """ Method to solve the nonogram.
        Returns solution as tuple of rows.
        """
        pass
                
    def show_grid(self):
        for row in self.__grid:
            print(' '.join(row))
            
if __name__=='__main__':
    clues = (((3,),(2,),(1,1),(1,1,1),(1,1,1)), #vertical
             ((2,),(1,),(1,3),(2,),(4,))) #horizontal
    solver = Nonogram(clues)
    solver.solve()
    solver.show_grid()