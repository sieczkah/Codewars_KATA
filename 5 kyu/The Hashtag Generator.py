"""https://www.codewars.com/kata/52449b062fb80683ec000024"""

def generate_hashtag(s):
    if len(s.replace(' ','')) > 140 or s.replace(' ','') == '':
        return False
    else:
        words = s.title().split()
        return f"#{''.join(words)}"
