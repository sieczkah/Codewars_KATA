"""https://www.codewars.com/kata/525c65e51bf619685c000059"""


def cakes(recipe, available):
    return min(available.get(item, 0) // recipe[item] for item in recipe.keys())