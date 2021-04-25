"""https://www.codewars.com/kata/59f08f89a5e129c543000069"""

def duplicate_filter(word):
    fitr_word = ''
    curr_char = ''
    for char in word:
        if curr_char == char:
            pass
        else:
            curr_char = char
            fitr_word += char
    return fitr_word

def dup(arry):
    return list(map(duplicate_filter, arry))
