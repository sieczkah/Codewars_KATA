"""https://www.codewars.com/kata/525821ce8e7b0d240b002615"""


from string import ascii_letters as asc

def camelize(str_):
    chars = asc + '0123456789'
    string = ''.join([x.lower() if x in chars else ' ' for x in str_]).split()
    string = ''.join(map(str.capitalize, string))
    return string
