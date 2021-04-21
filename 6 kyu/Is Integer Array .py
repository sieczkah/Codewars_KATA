"""https://www.codewars.com/kata/52a112d9488f506ae7000b95"""

def is_int_array(arr):
    try:
        x = [i % 1 == 0 for i in arr]
        return all(x) and isinstance(arr, list)
    except:
        return False

