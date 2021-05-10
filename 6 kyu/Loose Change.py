"""https://www.codewars.com/kata/5571f712ddf00b54420000ee"""

def loose_change(cents):
    money = {'Quarters': 25, 'Dimes': 10, 'Nickels': 5, 'Pennies': 1}
    if cents < 1:
        return {coin: 0 for coin in money.keys()}
    for coin, val in money.items():
        money[coin] = cents // val
        cents %= val
    return  money
        
