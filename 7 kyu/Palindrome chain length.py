"""https://www.codewars.com/kata/525f039017c7cd0e1a000a26/train/python"""


def palindrome_chain_length(n):
    steps = 0
    while str(n) != str(n)[::-1]:
        steps += 1
        n = n + int(str(n)[::-1])
    return steps
