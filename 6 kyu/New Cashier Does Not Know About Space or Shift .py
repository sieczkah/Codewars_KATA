"""https://www.codewars.com/kata/5d23d89906f92a00267bb83d/train/python"""


menu = ['Burger', 'Fries', "Chicken", 'Pizza', 'Sandwich', 'Onionrings',
       'Milkshake', 'Coke']
def get_order(order):
    return ''.join((i + ' ') * order.count(i.lower()) for i in menu).strip()
