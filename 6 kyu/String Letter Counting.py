"""https://www.codewars.com/kata/59e19a747905df23cb000024"""

from string import ascii_lowercase as letters
def string_letter_count(s):
    s = s.lower()
    return ''.join([f'{s.count(let)}{let}' for let in sorted(set(s)) if let in letters])
