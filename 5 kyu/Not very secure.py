"""https://www.codewars.com/kata/526dbd6c8c0eb53254000110"""

import re
def alphanumeric(password):
    return True if re.match('^[a-z0-9]+$', password, flags=re.IGNORECASE) else False
