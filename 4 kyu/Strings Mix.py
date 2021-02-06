"""https://www.codewars.com/kata/5629db57620258aa9d000014"""
def mix(s1, s2):
    all_letters = []
    for i in set([n for n in s1+s2 if n.islower()]):
        if s1.count(i) > 1 or s2.count(i) > 1:
            if s1.count(i) > s2.count(i):
                all_letters.append('1:' + i * s1.count(i))
            elif s1.count(i) < s2.count(i):
                all_letters.append('2:' + i * s2.count(i))
            else:
                all_letters.append(('=:' + i * s1.count(i)))
    
    return '/'.join(sorted(sorted(all_letters), key=len, reverse=True))
