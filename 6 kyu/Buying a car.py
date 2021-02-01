"""https://www.codewars.com/kata/554a44516729e4d80b000012"""


def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    months = 0
    saved = 0
    while saved + startPriceOld < startPriceNew:
        months += 1
        saved += savingperMonth
        if not months % 2:
            percentLossByMonth += 0.5
        startPriceNew *= (1 - (percentLossByMonth / 100))
        startPriceOld *= (1 - (percentLossByMonth / 100))
    return [months, round(saved + startPriceOld - startPriceNew)]
