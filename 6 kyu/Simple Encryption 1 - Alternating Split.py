"""https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python"""


def decrypt(encrypted_text, n):
    for _ in range(n):
        odd_pos = encrypted_text[len(encrypted_text) // 2:]
        even_pos = encrypted_text[:len(encrypted_text) // 2]
        word = ''.join([odd_pos[i] + even_pos[i] for i in range(len(even_pos))])
        if len(even_pos) != len(odd_pos):
            word += odd_pos[-1]
        encrypted_text = word
    return encrypted_text
        

def encrypt(text, n):
    for _ in range(n):
        even_pos = text[1::2]
        odd_pos = text[::2]
        text = even_pos + odd_pos
    return text
