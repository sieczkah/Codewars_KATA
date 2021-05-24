"""https://www.codewars.com/kata/5389864ec72ce03383000484"""

from string import ascii_lowercase as asc
import re

def autocomplete(input_, dictionary):
    print(input_)
    pat = ''.join(s.lower() for s in input_ if s.lower() in asc)
    return list(filter(lambda x: re.match(f'^{pat}', x.lower()), dictionary))[:5]
