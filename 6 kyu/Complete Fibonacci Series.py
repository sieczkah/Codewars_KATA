"""https://www.codewars.com/kata/5239f06d20eeab9deb00049b"""

def fibonacci(n):
    if n <= 1:
        return [0] if n == 1 else []
    else:
        fib = [0, 1]
        for _ in range(n - 2):
            fib.append(fib[-1] + fib[-2])
        return fib
