from models import Prayer, Groups
import datetime
from django.utils.timezone import utc
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth

def humanizeTimeDiff(timestamp = None):
    """
    Returns a humanized string representing time difference
    between now() and the input timestamp.
    
    The output rounds up to days, hours, minutes, or seconds.
    4 days 5 hours returns '4 days'
    0 days 4 hours 3 minutes returns '4 hours', etc...
    """
    import datetime
    
    timeDiff = datetime.datetime.utcnow().replace(tzinfo=utc) - timestamp
    days = timeDiff.days
    hours = timeDiff.seconds/3600
    minutes = timeDiff.seconds%3600/60
    seconds = timeDiff.seconds%3600%60
    
    str = ""
    tStr = ""
    if days > 0:
        if days == 1:   tStr = "day"
        else:           tStr = "days"
        str = str + "%s %s" %(days, tStr)
        return str
    elif hours > 0:
        if hours == 1:  tStr = "hour"
        else:           tStr = "hours"
        str = str + "%s %s" %(hours, tStr)
        return str
    elif minutes > 0:
        if minutes == 1:tStr = "min"
        else:           tStr = "mins"           
        str = str + "%s %s" %(minutes, tStr)
        return str
    elif seconds > 0:
        if seconds == 1:tStr = "sec"
        else:           tStr = "secs"
        str = str + "%s %s" %(seconds, tStr)
        return str
    else:
        return None

def calculate_time_diff(request, obj_list):
    timedifflist = {}
    for index, obj in enumerate(obj_list):
        timedifflist[index + 1] = humanizeTimeDiff(obj.timestamp)
    return timedifflist

def calc_top_groups():
    grouplist = Groups.objects.order_by("-prayer_count")
    return grouplist

def find_saved_groups(user):
    groups = Groups.objects.all()
    saved_groups = []
    for group in groups:
        if user in group.users_favorited.all():
            saved_groups.append(group)
    return saved_groups
