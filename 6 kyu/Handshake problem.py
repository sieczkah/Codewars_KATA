"""https://www.codewars.com/kata/5574835e3e404a0bed00001b"""

def get_participants(handshakes):
    n = 1
    while handshakes > 0:
        handshakes -= n
        n += 1
    return n
    
