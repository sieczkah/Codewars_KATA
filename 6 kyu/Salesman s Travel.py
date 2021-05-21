"""https://www.codewars.com/kata/56af1a20509ce5b9b000001e"""

def travel(r, zipcode):
    if zipcode == '':
        return ':/'
    places = [x.rstrip(zipcode).split() for x in r.split(',') if x.endswith(zipcode)]
    streets, numbers = [], []
    for pl in places:
        streets.append(' '.join(pl[1:]))
        numbers.append(pl[0])
    return zipcode + ':' + ','.join(streets) + '/' + ','.join(numbers)

