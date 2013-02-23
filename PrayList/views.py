from forms import PrayerForm
from models import Prayer
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
import datetime
from django.utils.timezone import utc
from django.template import RequestContext

def submit(request):
	if request.method == "POST":
		form = PrayerForm(request.POST)
		if form.is_valid():
			dt = datetime.datetime.now()
			dtclean = dt.strftime('%Y-%m-%d %H:%M:%S')
			p= Prayer(subject = request.POST['subject'], prayer = request.POST['prayer'], timestamp=dtclean)
			p.save()
			post = Prayer.objects.get(timestamp=dtclean)
			postid = post.id
			return HttpResponseRedirect('/post/' + str(postid) +'/')
	else:
		form = PrayerForm()
	return render_to_response('submit.html', {'form': form})

def new(request):
    obj_list = Prayer.objects.order_by("-id")
    timedifflist = calculate_time_diff(request, obj_list)
    path = request.get_full_path
    dt = datetime.datetime.now()
    dtclean = dt.strftime('%Y-%m-%d %H:%M:%S') 
    return render_to_response('new.html', {'prayers': obj_list, 'timestamps': timedifflist, 'current_time': dtclean, 'path': path})

def post_page(request, postid):
	prayer = Prayer.objects.get(id=postid)
	subject = prayer.subject
	timestamp = prayer.timestamp
	prayer = prayer.prayer
	return render_to_response('post_page.html', {'subject': subject, 'timestamp': timestamp, 'prayer': prayer})

# def top(request):
#     path = request.get_full_path
#     obj_list = Prayer.objects.order_by("-id")
#     timedifflist = calculate_time_diff(request, obj_list)
#     timediff_today = []
#     for item in timedifflist:
#         if "day" not in item:
#             timediff_today.append(item)
#     item_length = len(timediff_today)
#     new_obj_list = obj_list[:item_length]
#     return render_to_response('top_page.html', {'prayers': new_obj_list})



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