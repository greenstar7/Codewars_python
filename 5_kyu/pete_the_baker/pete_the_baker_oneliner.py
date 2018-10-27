''' Hrynevych Artemii
My oneliner version of solution for the "Pete, the baker" kata
https://www.codewars.com/kata/525c65e51bf619685c000059'''
# It's not as readable as the normal version
# But i just want it to be here
def cakes(recipe, available):
    ''' Function that calculates amount of cakes we can bake
    according to the recipe from the products that are available'''
    # using // division to get the integer result
    return min(available.get(key, 0)//recipe[key] for key in recipe)