"""https://www.codewars.com/kata/56484848ba95170a8000004d"""

def gps(s, x):
    speed = [(x[i + 1] - x[i]) / s * 3600 for i in range(len(x)-1)]
    return max(speed) if speed else 0

