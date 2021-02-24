"""https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python"""


def div_con(x):
    str_sum = sum(int(i) for i in x if type(i) == str)
    int_sum = sum(i for i in x if type(i) == int)
    return int_sum - str_sum
