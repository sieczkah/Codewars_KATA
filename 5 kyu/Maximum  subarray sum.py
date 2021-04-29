"""https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c"""

def max_sequence(arr):
    prev_sub = []
    max_arr = [0]
    for elem in arr:
        temp_arr = prev_sub + [elem]
        if sum(temp_arr) > elem:
            prev_sub = temp_arr[:]
        else:
            prev_sub = [elem]
        if sum(prev_sub) > sum(max_arr):
            max_arr = prev_sub[:]
    return sum(max_arr)
    
