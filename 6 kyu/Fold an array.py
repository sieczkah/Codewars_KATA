"""https://www.codewars.com/kata/57ea70aa5500adfe8a000110"""


def fold_array(array, runs):
    for _ in range(runs):
        if len(array) < 2:
            return array
        elif len(array) % 2:
            arr = [array[i] + array[-1 - i] for i in range(len(array) // 2)]
            arr.append(array[len(array) // 2])
            array = arr
        else:
            arr = [array[i] + array[-1 - i] for i in range(len(array) // 2)]
            array = arr
    return array

