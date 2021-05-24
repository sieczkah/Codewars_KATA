"""https://www.codewars.com/kata/56548dad6dae7b8756000037"""

def what_is_the_time(time_in_mirror):
    h, m = (int(elem) for elem in time_in_mirror.split(':'))
    # the hard thing is the hour hand we need to change hour to angle on clock
    h_angle = h * 30 + (m / 60 * 30) # 1 hour is 30 degrees also need to add up the minutes
    # next step is to make a mirror view of the angle
    h_clock = int((360 - h_angle) // 30) # and transfer it back to hours
    if h_clock <= 0:
        h_clock = str(12 + h_clock).zfill(2)
    else:
        h_clock = str(int(h_clock)).zfill(2)
    if m != 0:
        m = 60 - m
    return f'{h_clock}:{str(m).zfill(2)}'
