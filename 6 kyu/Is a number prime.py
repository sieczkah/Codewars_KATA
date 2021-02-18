"""https://www.codewars.com/kata/5262119038c0985a5b00029f"""


def is_prime(numb):
    print(numb)
    if numb < 2:
        return False
    else:
        for i in range(2, int(numb ** 0.5) + 1):
            if numb % i == 0 and i != numb:
                return False
        return True
