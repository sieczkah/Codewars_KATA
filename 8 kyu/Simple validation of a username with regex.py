"""https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023/solutions/python/me/best_practice"""

import re

def validate_usr(username):
    print(username)
    return bool(re.match(r'^[a-z0-9_]{4,16}$', username))
