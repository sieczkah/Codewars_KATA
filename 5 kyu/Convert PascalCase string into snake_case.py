"""https://www.codewars.com/kata/529b418d533b76924600085d"""

from string import ascii_uppercase as up
def to_underscore(string):
    if isinstance(string, str):
        return ''.join(['_' + c.lower() if c in up else c for c in string]).strip('_')
    else:
        return str(string)
