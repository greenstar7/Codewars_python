"""Hrynevych Artemii
My solution for the Codewars "Pete, the baker 2" kata
https://www.codewars.com/kata/5267e5827526ea15d8000708
"""

from math import ceil

def get_missing_ingredients(recipe, added):
    """Function to get the dictionary of the missing
    ingredients from the recipe that we havent added yet
    
    Arguments:
    recipe -- dict of "proguct: amount" needed for cooking
    added -- dict of "product: amount" already obtained
    """
    n_cakes = 0
    for ingredient in recipe:
        n_cakes = max(added.get(ingredient, 0)/recipe[ingredient], n_cakes)
    n_cakes = ceil(n_cakes)
    # the above "ceil" can be substituted with:
    # n_cakes = int(n_cakes+1)
    result = {key: recipe[key]*n_cakes-added.get(key, 0) for key in recipe}
    # retur
    return {key:value for key, value in result.items() if value != 0}