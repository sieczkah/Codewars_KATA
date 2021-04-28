"""https://www.codewars.com/kata/52b7ed099cdc285c300001cd"""

def sum_of_intervals(intervals):
    list_intervals = []
    for start, end in intervals:
        interval = list(range(start, end))
        list_intervals += interval
    return len(set(list_intervals))
