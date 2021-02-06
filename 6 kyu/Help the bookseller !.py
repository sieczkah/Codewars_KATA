"""https://www.codewars.com/kata/54dc6f5a224c26032800005c"""
def stock_list(listOfArt, listOfCat):
    if not listOfArt or not listOfCat:
        return ''
    val = dict.fromkeys(listOfCat, 0)
    for cat, qty in map(lambda x: x.split(), listOfArt):
        if cat[0] in val.keys():
            val[cat[0]] += int(qty)
    return ' - '.join([f'({k} : {val[k]})' for k in val.keys()])
