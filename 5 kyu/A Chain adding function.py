"""https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python"""


class add(int):
    def __call__(self, v):
        return add(self + v)
