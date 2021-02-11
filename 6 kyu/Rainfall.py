"""https://www.codewars.com/kata/56a32dd6e4f4748cc3000006/train/python"""


def mean(town, strng):
    data = strng.replace('\n', ':').split(':')
    if town not in data:
        return -1
    town_data = data[data.index(town) + 1]
    temps = [float(i[4:]) for i in town_data.split(',')]
    return sum(temps) / 12


def variance(town, strng):
    data = strng.replace('\n', ':').split(':')
    if town not in data:
        return -1
    temps = [float(i[4:]) for i in data[data.index(town) + 1].split(',')]
    avrg = sum(temps) / 12
    return sum(map(lambda x: (x - avrg) ** 2, temps)) / 12
