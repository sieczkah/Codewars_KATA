"""https://www.codewars.com/kata/52a89c2ea8ddc5547a000863"""

def loop_size(node):
    onestep = node
    twostep = node.next
    while(onestep != twostep):
        twostep = twostep.next.next
        onestep = onestep.next
    onestep = onestep.next
    size = 1
    while(onestep != twostep):
        size += 1
        onestep = onestep.next
    return size
