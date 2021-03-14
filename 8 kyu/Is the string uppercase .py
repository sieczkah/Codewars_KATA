"""https://www.codewars.com/kata/56cd44e1aa4ac7879200010b"""

from string import ascii_lowercase


def is_uppercase(inp):
    return all([i not in ascii_lowercase for i in inp])
