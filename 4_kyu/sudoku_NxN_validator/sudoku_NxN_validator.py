"""Hrynevych Artemii
My solution for the "Validate Sudoku with size `NxN`" kata
https://www.codewars.com/kata/validate-sudoku-with-size-nxn/
"""


class Sudoku(object):
    """Sudoku class to store the solved sudoku grid and validate it."""
    
    def __init__(self, grid):
        """Initializing the sudoku grid to validate
        and computing N -- side size of the grid
        
        Arguments:
        grid -- NxN sudoku grid
        """
        self.__grid = grid
        self.__N = len(grid)
        self.__alphabet = set(range(1, self.__N+1))
        
    def is_valid(self):
        """Method to check the solved sudoku."""
        if not self.check_dimensions():
            return False
        if not self.check_type():
            return False
        if not self.check_rows():
            return False
        if not self.check_columns():
            return False
        if not self.check_squares():
            return False
        return True

    def check_dimensions(self):
        """Function to check dimensions of the grid"""
        for row in self.__grid:
            if len(row) != self.__N:
                return False  
        return True
    
    def check_type(self):
        """Function to check types of all cells in grid"""
        for row in self.__grid:
            for element in row:
                if not isinstance(element, int) or isinstance(element, bool):
                    return False
        return True
                
    def check_rows(self):
        """Function to check if rows contain all elements
        of alphabet and only them"""
        for row in self.__grid:
            if set(row) != self.__alphabet:
                return False
        return True
            
    def check_columns(self):
        """Function to check if columns contain all elements 
        of alphabet and only them"""
        for col in range(self.__N):
            col_set = set()
            for row in range(self.__N):
                col_set.add(self.__grid[row][col])
            if col_set != self.__alphabet:
                return False
        return True
            
    def check_squares(self):
        """Function to check if squares contain all elements 
        of alphabet and only them"""
        from math import sqrt
        n = int(sqrt(self.__N))
        for i in range(n):
            rows = self.__grid[n*i:n*i+n]
            for j in range(n):
                square_set = {el for row in rows for el in row[n*j:n*j+n] }
                if square_set != self.__alphabet:
                    return False
        return True
