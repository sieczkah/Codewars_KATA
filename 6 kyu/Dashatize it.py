"""https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python"""


import re

def dashatize(n):
    s = re.findall(r'[24680]+|[13579]{1}', str(n))
    return '-'.join(s) if s else 'None'

