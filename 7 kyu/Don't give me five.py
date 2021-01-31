"""https://www.codewars.com/kata/5813d19765d81c592200001a"""

def dont_give_me_five(start,end):
    n = [i for i in range(start, end + 1) if '5' not in str(i)]
    return len(n)
