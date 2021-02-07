"""https://www.codewars.com/kata/526989a41034285187000de4/train/python"""
def ips_between(start, end):
    start_list = [int(x) for x in start.split('.')]
    end_list = [int(x) for x in end.split('.')]
    diff = [(end_list[i] - start_list[i]) * (256 ** (3-i)) for i in range(4)]
    return sum(diff)
