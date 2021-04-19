"""https://www.codewars.com/kata/5340298112fa30e786000688"""

def twos_difference(lst): 
    x = set(lst)
    return sorted([(i, i+2) for i in x if i+2 in x], key=sum)

