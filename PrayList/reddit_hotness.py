from datetime import datetime, timedelta
from math import log

epoch = datetime(1970, 1, 1)

def epoch_seconds(date):
    """Returns the number of seconds from the epoch to date."""
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

def hot(prayerscore, date):
    """The hot formula. Should match the equivalent function in postgres."""
    order = log(max(abs(prayerscore), 1), 10)
    sign = 1 if prayerscore > 0 else -1 if prayerscore < 0 else 0
    seconds = epoch_seconds(date) - 1134028003
    return round(order + sign * seconds / 45000, 7)