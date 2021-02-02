"""https://www.codewars.com/kata/559536379512a64472000053"""

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def play_pass(s, n):
    word = ''
    for sign in list(s):
        if sign.isalpha():
            letter_shift = (letters.find(sign) + n) % len(letters)
            word += letters[letter_shift]
        elif sign.isdigit():
            word += str(9 - int(sign))
        else:
            word += sign
    return ''.join([word[i].lower() if word[i].isalpha() and i % 2 else word[i] for i in range(len(word))])[::-1]
