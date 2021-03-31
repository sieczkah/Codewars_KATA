"""https://www.codewars.com/kata/56b7251b81290caf76000978"""

def get_last_digit(index):
    fib = [0, 1]
    for i in range(2, index + 1):
        fib.append(fib[-2] + fib[-1])
    return int(str(fib[-1])[-1])
