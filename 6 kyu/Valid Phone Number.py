"""https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/python"""


import re

def validPhoneNumber(phoneNumber):
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
    return bool(re.findall(pattern, phoneNumber))
