import re

# *---------Global Variables---------*
# URLs
homeURL = "http://127.0.0.1:8000/"
newURL = "http://127.0.0.1:8000/new/"
top_today_URL = "http://127.0.0.1:8000/top/"
top_week_URL = "http://127.0.0.1:8000/top/week/"
top_month_URL = "http://127.0.0.1:8000/top/month/"
top_year_URL = "http://127.0.0.1:8000/top/year/"
top_all_URL = "http://127.0.0.1:8000/top/all/"

# Functions
def equate_time(item):
    if("hour" in item):
        intval = re.sub("[a-zA-Z ]", "", item).strip()
        intval_clean = int(intval)
        return intval_clean
    elif("day" in item):
        intval = re.sub("[a-zA-Z ]", "", item).strip()
        intval_clean = int(intval) * 24
        return intval_clean
    elif("week" in item):
        intval = re.sub("[a-zA-Z ]", "", item).strip()
        intval_clean = int(intval) * 24 * 7
        return intval_clean
