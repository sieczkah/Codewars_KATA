"""https://www.codewars.com/kata/55beec7dd347078289000021/train/python"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    if node:
        length = 1
        while node.next:
            length += 1
            node = node.next
        return length
    else:
        return 0
    
def count(node, data):
    occur  = 0
    while node is not None:
        if node.data == data:
            occur += 1
        node = node.next
    return occur
