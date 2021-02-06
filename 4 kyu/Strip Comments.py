"""https://www.codewars.com/kata/51c8e37cee245da6b40000bd"""
def solution(string,markers):
    string_list = string.split('\n')
    for n in range(len(string_list)):
        for i in markers:
            if i in string_list[n]:
                a = string_list[n]
                string_list[n] = a[:a.find(i)].rstrip()
    return '\n'.join(string_list)
