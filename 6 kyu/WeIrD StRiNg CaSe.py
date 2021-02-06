"""https://www.codewars.com/kata/52b757663a95b11b3d00062d"""
def to_weird_case(string):
    words = string.split()
    for no, word in enumerate(words):
        words[no] = ''.join([word[l] if l % 2 else word[l].upper() for l in range(len(word))])
    return ' '.join(words)
