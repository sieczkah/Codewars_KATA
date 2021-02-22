"""https://www.codewars.com/kata/5848565e273af816fb000449/train/python"""


def encrypt_this(text):
    enc_text = []
    for i in text.split():
        if len(i) == 1:
            enc_text.append(str(ord(i)))
        elif len(i) < 3:
            enc_text.append(str(ord(i[0])) + i[-1])
        else:
            enc_text.append(str(ord(i[0])) + i[-1] + i[2:-1] + i[1])
    return ' '.join(enc_text)
