"""https://www.codewars.com/kata/5efae11e2d12df00331f91a6"""

from hashlib import md5
def crack(hash):
    pin_no = 0
    pin_str = str(pin_no).zfill(5)
    pin_hash = md5(pin_str .encode()).hexdigest()
    while pin_hash != hash:
        pin_no += 1
        pin_str = str(pin_no).zfill(5)
        pin_hash = md5(pin_str.encode()).hexdigest()

    return pin_str
