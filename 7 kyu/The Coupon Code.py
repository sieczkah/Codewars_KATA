"""https://www.codewars.com/kata/539de388a540db7fec000642/train/python"""


from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    cur = datetime.strptime(current_date, '%B %d, %Y')
    exp = datetime.strptime(expiration_date, '%B %d, %Y')
    return all([entered_code is correct_code, cur <= exp])
