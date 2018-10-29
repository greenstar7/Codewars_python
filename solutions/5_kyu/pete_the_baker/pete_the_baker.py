''' Hrynevych Artemii
My solution for the Codewars "Pete, the baker" kata
https://www.codewars.com/kata/525c65e51bf619685c000059'''

from math import floor

def cakes(recipe, available):
    ''' Function that calculates amount of cakes we can bake
    according to the recipe from the products that are available'''
    # check if all products from recipe are available
    for product in recipe:
        if product not in available:
            # if something is absent we can't cook
            return 0
    # and now, when we know, that all products are available
    # we must check how many cakes we can do from their amount
    # amount of product available / amount of it in recipe
    # gives as the numbee of cakes we can go from it
    cakes_number = []
    for k, v in recipe.items():
        cakes_number.append(available[k]/v)
    # the floored minimum number of cakes
    # is what we are looking for
    return floor(min(cakes_number))