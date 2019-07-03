""" Hrynevych Artemii
Tests for my 'Coloured Triangles' kata solution.

"""
from coloured_triangles import triangle

def test_triangle():
    assert triangle('B') == 'B'
    assert triangle('GB') == 'R'
    assert triangle('RRR') == 'R'
    assert triangle('RGBG') == 'B'
    assert triangle('RBRGBRB') == 'G'
    assert triangle('RBRGBRBGGRRRBGBBBGG') == 'G'

