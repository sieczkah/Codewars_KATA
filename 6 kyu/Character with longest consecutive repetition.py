"""https://www.codewars.com/kata/586d6cefbcc21eed7a001155"""

def longest_repetition(chars):
    char_list = []
    substrng = ''
    curr_char = ''
    for char in chars:
        if char == curr_char:
            substrng += char
        else:
            char_list.append((curr_char, len(substrng)))
            curr_char = char
            substrng = char
    char_list.append((curr_char, len(substrng)))
    return sorted(char_list, key=lambda x: -x[-1])[0]
