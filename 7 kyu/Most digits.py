"""https://www.codewars.com/kata/58daa7617332e59593000006/python"""



def find_longest(arr):
    max_lngth = len(str(max(arr)))
    for i in arr:
        if len(str(i)) == max_lngth:
            return i 


# shorter solution with max key and lambda func
def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))
