"""https://www.codewars.com/kata/52180ce6f626d55cf8000071"""

def str_to_hash(st):
    hash = {}
    if st:
        for vals in st.split(', '):
            letter, val = vals.split('=')
            hash[letter] = int(val)
    return hash
