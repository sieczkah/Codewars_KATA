"""https://www.codewars.com/kata/5a1a144f8ba914bbe800003f/train/python"""

def decipher_message(message):
    lng = int(len(message) ** 0.5) # the coding square is always perfect so we need to know the lenght
    words = [message[i::lng] for i in range(lng)] # in 5x5 we take every 5th letter in 6x6 we take every 6th...
    return ''.join(words)
