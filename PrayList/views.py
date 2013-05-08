from forms import PrayerForm, GroupForm
from models import Prayer, Groups
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect, HttpResponse
import datetime
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from pytz import timezone
from reddit_hotness import hot
from tagging.models import Tag, TaggedItem
from django.forms.util import ErrorList
from django.utils.safestring import mark_safe
import helper_func

def submit(request, group_name="none"):
    if request.user.is_authenticated():
        top_groups = helper_func.calc_top_groups()
        saved_groups = helper_func.find_saved_groups(request.user)
        path = request.path
        if request.method == "POST":
            form = PrayerForm(request.POST)
            if form.is_valid():
                dt = datetime.datetime.now()
                dtclean = dt.strftime('%Y-%m-%d %H:%M:%S')
                hotness = hot(0, dt)
                try:
                    group = Groups.objects.get(groupname=request.POST['group'])
                except Groups.DoesNotExist:
                    form._errors["group"] = ErrorList([request.POST['group'] + u" does not exist"])
                    return render_to_response('submit.html', {'form': form, 'user': request.user, 'doesnotexist': True, 'top_groups': top_groups, 'saved_groups': saved_groups}, context_instance=RequestContext(request))
                p= Prayer(subject = request.POST['subject'], prayer = request.POST['prayer'], timestamp=dtclean, prayerscore=0, hotness=hotness, group=group)
                p.save()
                group.prayer_count += 1
                group.total_hotness = calc_group_hotness(group)
                group.save()
                post = Prayer.objects.get(timestamp=dtclean)
                postid = post.id
                return HttpResponseRedirect('/post/' + str(postid) +'/')
        else:
            if "group" in path:
                form = PrayerForm(initial={'group': group_name})
            else: 
                form = PrayerForm()
        return render_to_response('submit.html', {'form': form, 'user': request.user, 'top_groups': top_groups, 'saved_groups': saved_groups}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/accounts/login/?next=/submit/")

def submit_group(request):
    if request.user.is_authenticated():
        top_groups = helper_func.calc_top_groups()
        saved_groups = helper_func.find_saved_groups(request.user)
        if request.method == "POST":
            form = GroupForm(request.POST)
            if form.is_valid():
                group= Groups(groupname= request.POST['group'], privacy= request.POST['privacy'])
                group.save()
                groupname = request.POST['group']
                return HttpResponseRedirect('/submitgroup/' + str(groupname) + '/success/')
        else:
            form = GroupForm()
        return render_to_response('submitgroup.html', {'form': form, 'user': request.user, 'top_groups': top_groups, 'saved_groups': saved_groups}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/accounts/login/?next=/submitgroup/')

def submit_group_success(request, groupname):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    group_name = groupname
    return render_to_response('submitgroupsuccess.html', {'groupname': group_name, 'user': request.user, 'top_groups': top_groups, 'saved_groups': saved_groups}, context_instance=RequestContext(request))

def new(request, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    obj_list = Prayer.objects.order_by("-id")[count_int:count_next]
    timedifflist = helper_func.calculate_time_diff(request, obj_list)
    path = request.get_full_path
    root_path = "/new"
    dt = datetime.datetime.now()
    dtclean = dt.strftime('%Y-%m-%d %H:%M:%S') 
    return render_to_response('new.html', {'prayers': obj_list, 'timestamps': timedifflist, 'current_time': dtclean, 'path': path, 'user': request.user, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path})

def post_page(request, postid):
    if request.is_ajax():
        prayer = Prayer.objects.get(id=postid)
        prayer.prayerscore = int(prayer.prayerscore) + 1
        prayer.prayed_users.add(request.user)
        prayer.save()
        return HttpResponse(status=200)
    else:
        top_groups = helper_func.calc_top_groups()
        saved_groups = helper_func.find_saved_groups(request.user)
        date = datetime.datetime.now()
        prayed = False
        prayer = Prayer.objects.get(id=postid)
        users = prayer.prayed_users
        subject = prayer.subject
        timestamp = prayer.timestamp.astimezone(timezone('US/Central'))
        timestampdt = datetime.datetime(timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second)
        prayer_post = prayer.prayer
        this_group = Groups.objects.get(groupname=prayer.group.groupname)
        this_group_name = this_group.groupname
        pid = postid
        prayer_score = prayer.prayerscore
        prayer.hotness = hot(prayer_score, timestampdt)
        prayer.save()
        return render_to_response('post_page.html', 
                                 {'prayerscore': prayer_score, 'users': users, 
                                  'subject': subject, 'timestamp': timestamp, 
                                    'prayer': prayer_post, 'userid': request.user, 
                                    'path': request.get_full_path, 'id': postid,
                                    'top_groups': top_groups, 'saved_groups': saved_groups, 'this_group': this_group_name
                                    }, 
                                        context_instance=RequestContext(request)
                                   )
    


def top_today(request, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    path = request.get_full_path
    root_path = "/top/today"
    obj_list = Prayer.objects.order_by("-prayerscore")[count_int:count_next]
    dt = datetime.datetime.now(timezone('US/Central'))
    today = dt.strftime('%Y-%m-%d') 
    new_obj_list = []
    for prayer in obj_list:
        newstamp = prayer.timestamp.astimezone(timezone('US/Central'))
        if newstamp.strftime('%Y-%m-%d') == today:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'today': today, 'user': request.user, 'path': path, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path})

def top_alltime(request, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    path = request.get_full_path
    root_path = "/top/all"
    obj_list = Prayer.objects.order_by("-prayerscore")[count_int:count_next]
    dt = datetime.datetime.now()
    today = dt.strftime('%Y-%m-%d') 
    return render_to_response('top_page.html', {'prayers': obj_list, 'today': today, 'user': request.user, 'path': path, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path})

def top_month(request, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    path = request.get_full_path
    root_path = "/top/month"
    obj_list = Prayer.objects.order_by("-prayerscore")[count_int:count_next]
    dt = datetime.datetime.now()
    month = dt.strftime('%m') 
    new_obj_list = []
    for prayer in obj_list:
        if prayer.timestamp.strftime('%m') == month:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'user': request.user, 'path': path, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path})


def top_year(request, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    path = request.get_full_path
    root_path = "/top/year"
    obj_list = Prayer.objects.order_by("-prayerscore")[count_int:count_next]
    dt = datetime.datetime.now()
    year = dt.strftime('%Y') 
    new_obj_list = []
    for prayer in obj_list:
        if prayer.timestamp.strftime('%Y') == year:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'user': request.user, 'path': path, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path})

def top_week(request, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    path = request.get_full_path
    root_path = "/top/week"
    obj_list = Prayer.objects.order_by("-prayerscore")[count_int:count_next]
    dt = datetime.datetime.now()
    week = dt.isocalendar()[1]
    new_obj_list = []
    for prayer in obj_list:
        if prayer.timestamp.isocalendar()[1] == week:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'user': request.user, 'path': path, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path})    

def logout_view(request):
    logout(request)
    # Redirect to a homepage.
    return HttpResponseRedirect("/new/")

def voted(request, postid): 
    if request.user.is_authenticated():
        prayer = Prayer.objects.get(id=postid)
        prayer.prayerscore = int(prayer.prayerscore) + 1
        prayer.prayed_users.add(request.user)
        prayer.save()
        return HttpResponse(status=200)
    else:
        return HttpResponseRedirect("/accounts/login/?next=/post/" + postid + "/")

def register(request):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
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
            return render_to_response("register.html", {
            'form': form, 'top_groups': top_groups, 'saved_groups': saved_groups, 'errors': form.errors
        }, context_instance=RequestContext(request))
    else:
        form = UserCreationForm()
        return render_to_response("register.html", {
            'form': form, 'top_groups': top_groups, 'saved_groups': saved_groups
        }, context_instance=RequestContext(request))

def trending(request, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    obj_list = Prayer.objects.order_by("-hotness")[count_int:count_next]
    timedifflist = helper_func.calculate_time_diff(request, obj_list)
    path = request.get_full_path
    root_path = ""
    dt = datetime.datetime.now()
    dtclean = dt.strftime('%Y-%m-%d %H:%M:%S') 
    return render_to_response('new.html', {'prayers': obj_list, 'timestamps': timedifflist, 'current_time': dtclean, 'path': path, 'user': request.user, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path})

def groups(request, group, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    path = request.get_full_path
    root_path = "/group/" +  group 
    thegroup = Groups.objects.get(groupname=group)
    obj_list = Prayer.objects.filter(group = thegroup)[count_int:count_next]
    return render_to_response('new.html', {'prayers': obj_list, 'user': request.user, 'path': path, 'groupname': group, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path})      

def groups_new(request, group, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    path = request.get_full_path
    root_path = "/group/" +  group + "/new"
    thegroup = Groups.objects.get(groupname=group)
    obj_list = Prayer.objects.filter(group = thegroup).order_by("-id")[count_int:count_next]
    return render_to_response('new.html', {'prayers': obj_list, 'user': request.user, 'path': path, 'groupname': group, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path}) 

def groups_top_today(request, group, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    path = request.get_full_path
    root_path = "/group/" +  group + "/top/today"
    thegroup = Groups.objects.get(groupname=group)
    obj_list = Prayer.objects.filter(group = thegroup).order_by("-prayerscore")[count_int:count_next]
    dt = datetime.datetime.now(timezone('US/Central'))
    today = dt.strftime('%Y-%m-%d') 
    new_obj_list = []
    for prayer in obj_list:
        newstamp = prayer.timestamp.astimezone(timezone('US/Central'))
        if newstamp.strftime('%Y-%m-%d') == today:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'today': today, 'user': request.user, 'path': path, 'groupname': group, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path}) 

def groups_top_week(request, group, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    path = request.get_full_path
    root_path = "/group/" +  group + "/top/week"
    thegroup = Groups.objects.get(groupname=group)
    obj_list = Prayer.objects.filter(group = thegroup).order_by("-prayerscore")[count_int:count_next]
    dt = datetime.datetime.now(timezone('US/Central'))
    today = dt.strftime('%Y-%m-%d') 
    week = dt.isocalendar()[1]
    new_obj_list = []
    for prayer in obj_list:
        if prayer.timestamp.isocalendar()[1] == week:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'today': today, 'user': request.user, 'path': path, 'groupname': group, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path}) 

def groups_top_month(request, group, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    path = request.get_full_path
    root_path = "/group/" +  group + "/top/month"
    thegroup = Groups.objects.get(groupname=group)
    obj_list = Prayer.objects.filter(group = thegroup).order_by("-prayerscore")[count_int:count_next]
    dt = datetime.datetime.now(timezone('US/Central'))
    today = dt.strftime('%Y-%m-%d') 
    month = dt.strftime('%m') 
    new_obj_list = []
    for prayer in obj_list:
        if prayer.timestamp.strftime('%m') == month:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'today': today, 'user': request.user, 'path': path, 'groupname': group, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path})

def groups_top_year(request, group, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    root_path = "/group/" +  group + "/top/year"
    path = request.get_full_path
    thegroup = Groups.objects.get(groupname=group)    
    obj_list = Prayer.objects.filter(group = thegroup).order_by("-prayerscore")[count_int:count_next]
    dt = datetime.datetime.now(timezone('US/Central'))
    today = dt.strftime('%Y-%m-%d') 
    year = dt.strftime('%Y') 
    new_obj_list = []
    for prayer in obj_list:
        if prayer.timestamp.strftime('%Y') == year:
            new_obj_list.append(prayer)
    return render_to_response('top_page.html', {'prayers': new_obj_list, 'today': today, 'user': request.user, 'path': path, 'groupname': group, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path})

def groups_top_all(request, group, count=0):
    top_groups = helper_func.calc_top_groups()
    saved_groups = helper_func.find_saved_groups(request.user)
    count_int = int(count)
    count_next = count_int+10
    path = request.get_full_path
    root_path = "/group/" +  group + "/top/all"
    thegroup = Groups.objects.get(groupname=group)    
    obj_list = Prayer.objects.filter(group = thegroup).order_by("-prayerscore")[count_int:count_next]
    dt = datetime.datetime.now(timezone('US/Central'))
    today = dt.strftime('%Y-%m-%d') 
    return render_to_response('top_page.html', {'prayers': obj_list, 'today': today, 'user': request.user, 'path': path, 'groupname': group, 'top_groups': top_groups, 'saved_groups': saved_groups, 'count': count_int, 'count_next': count_next, 'root_path': root_path})

def managegroups(request, groupid="none"):        
    if request.user.is_authenticated():
        if request.is_ajax():
            if "unsubscribe" in request.path:
                group = Groups.objects.get(id=groupid)
                group.users_favorited.remove(request.user)
                group.save()
                return HttpResponse(status=200)
            else:
                group = Groups.objects.get(id=groupid)
                group.users_favorited.add(request.user)
                group.save()
                return HttpResponse(status=200)
        else:
            top_groups = helper_func.calc_top_groups()
            saved_groups = helper_func.find_saved_groups(request.user)
            return render_to_response('managegroups.html', {'top_groups': top_groups, 'saved_groups': saved_groups, 'user': request.user}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/accounts/login/?next=/managegroups/")

def my_praylist(request):
    if request.user.is_authenticated():
        return render_to_response('mypraylist.html', {'user':request.user})
