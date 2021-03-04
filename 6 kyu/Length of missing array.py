"""https://www.codewars.com/kata/57b6f5aadb5b3d0ae3000611/train/python"""

def get_length_of_missing_array(a):
    if any([None in a, [] in a, not a]):
        return 0    
    else:
        arr = [len(i) for i in a]
        complete = sum(list(range(min(arr), max(arr) +1)))
    return complete - sum(arr)
