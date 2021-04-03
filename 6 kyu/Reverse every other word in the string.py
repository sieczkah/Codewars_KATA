"""https://www.codewars.com/kata/58d76854024c72c3e20000de"""

def reverse_alternate(string):
    words = string.split()
    reversed = [words[i][::-1] if i % 2 else words[i] for i in range(len(words))]
    return ' '.join(reversed)
