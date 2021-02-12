"""https://www.codewars.com/kata/5b37a50642b27ebf2e000010/train/python"""


import re

def sum_of_a_beach(beach):
    com = re.compile(r'water|sand|fish|sun', flags= re.I)
    return len(com.findall(beach))
