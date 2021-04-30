"""https://www.codewars.com/kata/559a28007caad2ac4e000083"""

def perimeter(n):
    fib = [1, 1]
    for _ in range(n - 1):
        fib.append(fib[-1] + fib[-2])
    return sum(fib) * 4
