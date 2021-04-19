"""https://www.codewars.com/kata/52f787eb172a8b4ae1000a34"""

def zeros(n):
# Trailing zeroes are always produced by prime factors 2 and 5
# as there is always more 2s then 5s we can assume that trailing 
# zeroes are produced by 5
    count = 0
    while n >= 5:
        n //= 5
        count +=n
    return count
