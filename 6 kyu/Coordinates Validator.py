"""https://www.codewars.com/kata/5269452810342858ec000951"""

import re

def is_valid_coordinates(coordinates):
    cords = coordinates.split(',')
    if len(cords) != 2:
        return False
    lat = re.match('^-?(([0-8]?\d(\.\d*)?)|90){1}$', cords[0])
    lon = re.match('^ ?-?((1?[0-7]?\d(\.\d*)?)|180){1}$', cords[1])
    
    return True if all([lat, lon]) else False
