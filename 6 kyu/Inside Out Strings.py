"""https://www.codewars.com/kata/57ebdf1c2d45a0ecd7002cd5"""

def inside_out(st):
    words_list = st.split(' ')
    inside_out_list = []
    
    for word in words_list:
        length = len(word)

        if length % 2:
            # 0 1 2 3 4 - odd word indexes
            mid = word[length // 2]
            left = word[: length // 2]
            right = word[(length // 2) + 1 :]
            turned_word = left[::-1] + mid + right [::-1]
            inside_out_list.append(turned_word)
        else:
            # 0 1 2 3 4 5 - even word indexes
            left = word [ : length // 2]
            right = word[(length // 2) : ]
            turned_word = left[::-1] + right [::-1]
            inside_out_list.append(turned_word)
    
    return ' '.join(inside_out_list)
                    
