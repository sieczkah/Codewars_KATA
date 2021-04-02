"""https://www.codewars.com/kata/5898b4b71d298e51b600014b"""

def get_dsc_inner(word):
    if len(word) > 3:
        return word[0] + ''.join(sorted(word[1:-1], reverse=True)) + word[-1]
    else: 
        return word

def sort_the_inner_content(words):
    words_list = words.split()
    return ' '.join(get_dsc_inner(word) for word in words_list)
