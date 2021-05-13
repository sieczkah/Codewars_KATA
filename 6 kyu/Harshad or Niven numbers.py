"""https://www.codewars.com/kata/54a0689443ab7271a90000c6"""

class Harshad:
    @staticmethod
    def is_valid(number):
        return number % sum(int(i) for i in str(number)) == 0
    
    @staticmethod
    def get_next(number):
        next = number + 1
        while not Harshad.is_valid(next):
            next += 1
        return next
    
    @staticmethod
    def get_series(count, start=0):
        series = []
        while len(series) < count:
            start += 1
            if Harshad.is_valid(start):
                series.append(start)
        return series
