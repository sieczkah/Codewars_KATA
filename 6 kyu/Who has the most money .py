"""https://www.codewars.com/kata/528d36d7cc451cd7e4000339"""

def money_sum(student):
    return student.fives * 5 + student.tens * 10 + student.twenties * 20

def most_money(students):
    money_list = [(s.name, money_sum(s)) for s in students]
    money_list.sort(key=lambda x: x[1], reverse=True)
    if len(money_list) > 1:
        return 'all' if money_list[0][-1] == money_list[-1][-1] else money_list[0][0]
    else:
        return money_list[0][0]
