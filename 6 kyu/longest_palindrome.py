"""https://www.codewars.com/kata/54bb6f887e5a80180900046b"""

def longest_palindrome (s):
    lng = len(s)
    max_lng = 1
    for i in range(lng):
        # checking first even then odd lenght palindrome
        # expanding from middle of palindrome to left and right
        for left, right in [(i - 1, i), (i - 1, i + 1)]:
            while left >= 0 and right < lng and s[left] == s[right]:
                # checking if lnght of current palindrome is bigger than max
                if right - left + 1 > max_lng:
                    max_lng = right - left + 1
                # expanding to left and right
                left -= 1
                right += 1

    return max_lng if s else 0
