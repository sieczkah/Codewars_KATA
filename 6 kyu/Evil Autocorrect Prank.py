"""https://www.codewars.com/kata/538ae2eb7a4ba8c99b000439"""

import re

def autocorrect(input):
    pattern = re.compile(r'\b([yY]+[Oo]+[uU]+)\b|\b[uU]\b')
    return re.sub(pattern,'your sister', input)
