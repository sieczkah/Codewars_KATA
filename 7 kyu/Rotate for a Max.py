"""https://www.codewars.com/kata/56a4872cbb65f3a610000026/train/python"""


def max_rot(n):
    st_n = str(n)
    rot_lst = [n]
    for i in range(len(st_n) - 1):
        st_n = st_n[:i] + st_n[i + 1:] + st_n[i]
        rot_lst.append(st_n)
    return max(map(int, rot_lst))
