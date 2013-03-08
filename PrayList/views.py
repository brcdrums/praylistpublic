from forms import PrayerForm
from models import Prayer
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
import datetime
from django.utils.timezone import utc
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import authenticate, login
from pytz import timezone
from reddit_hotness import hot

def submit(request):
    if request.method == "POST":
        form = PrayerForm(request.POST)
        if form.is_valid():
            dt = datetime.datetime.now()
            dtclean = dt.strftime('%Y-%m-%d %H:%M:%S')
            hotness = hot(0, dt)
            p= Prayer(subject = request.POST['subject'], prayer = request.POST['prayer'], timestamp=dtclean, prayerscore=0, hotness=hotness, tags= request.POST['tags'])
            p.save()
            post = Prayer.objects.get(timestamp=dtclean)
            postid = post.id
            return HttpResponseRedirect('/post/' + str(postid) +'/')
    else:
        form = PrayerForm()
    return render_to_response('submit.html', {'form': form, 'user': request.user}, context_instance=RequestContext(request))

def new(request):
    obj_list = Prayer.objects.order_by("-id")
    timedifflist = calculate_time_diff(request, obj_list)
    path = request.get_full_path
    dt = datetime.datetime.now()
    dtclean = dt.strftime('%Y-%m-%d %H:%M:%S') 
    return render_to_response('new.html', {'prayers': obj_list, 'timestamps': timedifflist, 'current_time': dtclean, 'path': path, 'user': request.user})

def post_page(request, postid):
    date = datetime.datetime.now()
    prayed = False
    prayer = Prayer.objects.get(id=postid)
    users = prayer.prayed_users
    subject = prayer.subject
    timestamp = prayer.timestamp.astimezone(timezone('US/Central'))
    timestampdt = datetime.datetime(timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second)
    prayer_post = prayer.prayer
    pid = postid
    prayer_score = prayer.prayerscore
    prayer.hotness = hot(prayer_score, timestampdt)
    prayer.save()
    return render_to_response('post_page.html', 
                             {'prayerscore': prayer_score, 'users': users, 
                              'subject': subject, 'timestamp': timestamp, 
                              'prayer': prayer_post, 'userid': request.user, 
                              'path': request.get_full_path, 'id': postid}, 
                               context_instance=RequestContext(request)
                               )

def top_today(request):
    path = request.get_full_path
    obj_list = Prayer.objects.order_by("-prayerscore")
    dt = datetime.datetime.now(timezone('US/Central'))
    today = dt.strftime('%Y-%m-%d') 
    new_obj_list = []
    for prayer in obj_list:
        newstamp = prayer.timestamp.astimezone(timezone('US/Central'))
        if newstamp.strftime('%Y-%m-%d') == today:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'today': today, 'user': request.user, 'path': path})

def top_alltime(request):
    path = request.get_full_path
    obj_list = Prayer.objects.order_by("-prayerscore")
    dt = datetime.datetime.now()
    today = dt.strftime('%Y-%m-%d') 
    return render_to_response('top_page.html', {'prayers': obj_list, 'today': today, 'user': request.user, 'path': path})

def top_month(request):
    path = request.get_full_path
    obj_list = Prayer.objects.order_by("-prayerscore")
    dt = datetime.datetime.now()
    month = dt.strftime('%m') 
    new_obj_list = []
    for prayer in obj_list:
        if prayer.timestamp.strftime('%m') == month:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'user': request.user, 'path': path})


def top_year(request):
    path = request.get_full_path
    obj_list = Prayer.objects.order_by("-prayerscore")
    dt = datetime.datetime.now()
    month = dt.strftime('%Y') 
    new_obj_list = []
    for prayer in obj_list:
        if prayer.timestamp.strftime('%Y') == month:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'user': request.user, 'path': path})

def top_week(request):
    path = request.get_full_path
    obj_list = Prayer.objects.order_by("-prayerscore")
    dt = datetime.datetime.now()
    week = dt.isocalendar()[1]
    new_obj_list = []
    for prayer in obj_list:
        if prayer.timestamp.isocalendar()[1] == week:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'user': request.user, 'path': path})    

def logout_view(request):
    auth.logout(request)
    # Redirect to a homepage.
    return HttpResponseRedirect("/new/")

def voted(request, postid): 
    if request.user.is_authenticated():
        prayer = Prayer.objects.get(id=postid)
        prayer.prayerscore = int(prayer.prayerscore) + 1
        prayer.prayed_users.add(request.user)
        prayer.save()
        return HttpResponseRedirect("/post/" + str(postid) + "/")
    else:
        return HttpResponseRedirect("/accounts/login/?next=/post/" + postid + "/")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/new/")
    else:
        form = UserCreationForm()
    return render_to_response("register.html", {
        'form': form, 
    }, context_instance=RequestContext(request))

def trending(request):
    obj_list = Prayer.objects.order_by("-hotness")
    timedifflist = calculate_time_diff(request, obj_list)
    path = request.get_full_path
    dt = datetime.datetime.now()
    dtclean = dt.strftime('%Y-%m-%d %H:%M:%S') 
    return render_to_response('new.html', {'prayers': obj_list, 'timestamps': timedifflist, 'current_time': dtclean, 'path': path, 'user': request.user})


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