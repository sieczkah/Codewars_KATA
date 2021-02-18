"""https://www.codewars.com/kata/52742f58faf5485cae000b9a"""


def format_duration(seconds):
    if not seconds:
        return 'now'
    else:
        years = seconds // 31536000
        days = (seconds % 31536000) // 86400
        hours = seconds % 31536000 % 86400 // 3600
        minutes = seconds % 31536000 % 86400 % 3600 // 60
        seconds = seconds % 31536000 % 86400 % 3600 % 60
        years_str = None
        days_str = None
        hours_str = None
        minutes_str = None
        seconds_str = None
        if years != 0:
            years_str = f'{years} years' if years > 1 else '1 year'
        if days != 0:
            days_str = f'{days} days' if days > 1 else '1 day'
        if hours != 0:
            hours_str = f'{hours} hours' if hours > 1 else '1 hour'
        if minutes != 0:
            minutes_str = f'{minutes} minutes' if minutes > 1 else '1 minute'
        if seconds != 0:
            seconds_str = f'{seconds} seconds' if seconds > 1 else '1 second'
        end_str = [i for i in (years_str, days_str, hours_str, minutes_str, seconds_str) if i]
        if len(end_str) > 1:
            end_str.insert(-1, 'and')
        return ' '.join(end_str) if len(end_str) < 3 else ', '.join(end_str[:-2]) + ' ' + ' '.join(end_str[-2:])
