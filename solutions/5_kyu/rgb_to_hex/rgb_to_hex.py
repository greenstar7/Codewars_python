""" https://www.codewars.com/kata/rgb-to-hex-conversion solution """

def rgb(r, g, b):
    bounded = lambda x: max(min(x, 255), 0)
    hexed = lambda x: hex(bounded(x))[2:].upper()
    hex_colors = (hexed(color) for color in (r, g, b))
    return ''.join(((c if len(c) == 2 else '0'+c) for c in hex_colors))
