""" Hrynevych Artemii - solution for 'human readable duration format kata.

Kata assumes, that year has 365 days.

"""

unit_and_time = [
    ('year', 3600*24*365), ('day', 3600*24),
    ('hour', 3600), ('minute', 60), ('second', 1)
]


def format_duration(seconds):
    if seconds == 0:
        res = 'now'
    else:
        res = []
        for unit, time in unit_and_time:
            temp = seconds // time
            if temp == 1:
                res.append(str(temp) + ' ' + unit)
            elif temp > 1:
                res.append(str(temp) + ' ' + unit + 's')
            seconds = seconds % time
        if len(res) >= 2:
            last = res.pop()
            prev_last = res.pop()
            res.append(' and '.join((prev_last, last)))
        res = ', '.join(res)
    return res
