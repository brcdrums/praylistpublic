from forms import PrayerForm, GroupForm, NewCustomPrayer, CommentForm
from models import Prayer, Groups, UserProfile, SavedPrayerCustom, PrayedFor, Comments
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect, HttpResponse
import datetime
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from pytz import timezone
from reddit_hotness import hot
from tagging.models import Tag, TaggedItem
from django.forms.util import ErrorList
from django.utils.safestring import mark_safe
import helper_func
from itertools import chain


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
                    group = Groups.objects.get(groupname=request.POST['prayer_group'])
                except Groups.DoesNotExist:
                    form._errors["prayer_group"] = ErrorList([u"The group \'" + request.POST['prayer_group'] + u"\' does not exist"])
                    group_name = request.POST['prayer_group']
                    return render_to_response('submit.html', {'form': form, 'user': request.user, 'doesnotexist': True, 'top_groups': top_groups, 'saved_groups': saved_groups, 'group_name': group_name}, context_instance=RequestContext(request))
                p= Prayer(subject = request.POST['subject'], prayer = request.POST['prayer'], timestamp=dtclean, prayerscore=0, hotness=hotness, group=group)
                p.save()
                group.prayer_count += 1
                group.total_hotness = helper_func.calc_group_hotness(group)
                group.save()
                post = Prayer.objects.get(timestamp=dtclean)
                postid = post.id
                return HttpResponseRedirect('/post/' + str(postid) +'/')
        else:
            if "group" in path:
                form = PrayerForm(initial={'prayer_group': group_name})
            else: 
                form = PrayerForm()
        return render_to_response('submit.html', {'form': form, 'user': request.user, 'top_groups': top_groups, 'saved_groups': saved_groups}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/accounts/login/?next=/submit/")

def submit_group(request, group_name="none"):
    if request.user.is_authenticated():
        top_groups = helper_func.calc_top_groups()
        saved_groups = helper_func.find_saved_groups(request.user)
        if request.method == "POST":
            form = GroupForm(request.POST)
            if form.is_valid():
                if " " in request.POST['group']:
                    form._errors['group'] = ErrorList([u"Spaces are not allowed"])
                    return render_to_response('submitgroup.html', {'form': form, 'user': request.user, 'top_groups': top_groups, 'saved_groups': saved_groups, 'group_name': group_name}, context_instance=RequestContext(request))
                group= Groups(groupname= request.POST['group'], privacy= request.POST['privacy'])
                group.save()
                groupname = request.POST['group']
                return HttpResponseRedirect('/success/'+ str(groupname))
        else:
            data = {'group': group_name, 'privacy': 0}
            if group_name == "none":
                form = GroupForm()
            else:
                form = GroupForm(data)
        return render_to_response('submitgroup.html', {'form': form, 'user': request.user, 'top_groups': top_groups, 'saved_groups': saved_groups, 'group_name': group_name}, context_instance=RequestContext(request))
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
        if "add" in request.path:
            prayer = Prayer.objects.get(id=postid)
            userobj = User.objects.get(username=request.user)
            userobj.profile.saved_prayer.add(prayer)
            userobj.save()
            return HttpResponse(status=200)
        else:
            prayer = Prayer.objects.get(id=postid)
            prayer.prayerscore = int(prayer.prayerscore) + 1
            if request.user not in prayer.prayed_users.all():
                prayer.prayed_users.add(request.user)
            timestamp = prayer.timestamp.astimezone(timezone('US/Central'))
            timestampdt = datetime.datetime(timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second)
            prayer.hotness = hot(prayer.prayerscore, timestampdt)
            prayer.save()
            this_group = Groups.objects.get(groupname=prayer.group.groupname)
            this_group_name = this_group.groupname
            this_group.total_hotness = helper_func.calc_group_hotness(this_group)
            this_group.save()
            dt = datetime.datetime.now()
            dtclean = dt.strftime('%Y-%m-%d %H:%M:%S')  
            userobj = User.objects.get(username=request.user)
            prayedfor = PrayedFor(prayed_user=userobj, prayer=prayer, timestamp=dtclean)
            prayedfor.save()
            return HttpResponse(status=200)
    else:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                dt = datetime.datetime.now()
                dtclean = dt.strftime('%Y-%m-%d %H:%M:%S')
                prayer = Prayer.objects.get(id=postid)
                comment = Comments(prayer=prayer, body=request.POST['comment'], posted_on=dtclean, user=request.user)
                comment.save()
                return HttpResponseRedirect('')
        form = CommentForm()
        prayer = Prayer.objects.get(id=postid)
        comments = Comments.objects.filter(prayer=prayer).order_by("-posted_on")
        top_groups = helper_func.calc_top_groups()
        saved_groups = helper_func.find_saved_groups(request.user)
        date = datetime.datetime.now()
        userobj = User.objects.get(username=request.user)
        saved_prayers = userobj.profile.saved_prayer
        subject = prayer.subject
        timestamp = prayer.timestamp.astimezone(timezone('US/Central'))
        timestampdt = datetime.datetime(timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second)
        prayer_post = prayer.prayer
        this_group = Groups.objects.get(groupname=prayer.group.groupname)
        this_group_name = this_group.groupname
        prayer_score = prayer.prayerscore
        prayed = helper_func.has_prayed_today(userobj, prayer)
        return render_to_response('post_page.html', 
                                 {'prayerscore': prayer_score, 
                                  'subject': subject, 'timestamp': timestamp, 
                                    'prayer': prayer_post, 'prayerobj': prayer, 'userid': request.user, 'saved_prayers': saved_prayers,
                                    'path': request.get_full_path, 'id': postid,
                                    'top_groups': top_groups, 'saved_groups': saved_groups, 'this_group': this_group_name, 'prayed': prayed, 'form': form, 'comments': comments
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
    form = NewCustomPrayer(request.POST)
    if request.method == "POST":
        if form.is_valid:
            dt = datetime.datetime.now()
            dtclean = dt.strftime('%Y-%m-%d %H:%M:%S')
            userobj = User.objects.get(username=request.user)
            custom_p = request.POST['newprayer']
            new_p = SavedPrayerCustom(timestamp=dtclean, custom_prayer=custom_p, prayed_user=userobj)
            new_p.save()
        return HttpResponseRedirect('')
    if request.user.is_authenticated():
        top_groups = helper_func.calc_top_groups()
        saved_groups = helper_func.find_saved_groups(request.user)
        userobj = User.objects.get(username=request.user)
        saved_prayers = userobj.profile.saved_prayer
        saved_prayers_list = userobj.profile.saved_prayer.all()
        custom_prayers = SavedPrayerCustom.objects.filter(prayed_user=userobj)
        allprayers = chain(saved_prayers_list, custom_prayers)
        userprayers = PrayedFor.objects.filter(prayed_user=userobj)
        prayed_today = []
        dt = datetime.datetime.now()
        today = dt.strftime('%Y-%m-%d') 
        for obj in saved_prayers_list:
            if helper_func.has_prayed_today(userobj, obj):
                prayed_today.append(obj.id)
        for obj in custom_prayers:
            if helper_func.has_prayed_today(userobj, obj, True):
                prayed_today.append(obj.id)
        prayed_for_today = 0
        prayed_for_month = 0
        prayed_for_year = 0
        month = dt.strftime('%Y-%m')
        year = dt.strftime('%Y')
        for prayer in userprayers:
            if prayer.timestamp.astimezone(timezone('US/Central')).strftime('%Y-%m-%d') == today:
                prayed_for_today += 1
                prayed_for_month += 1
                prayed_for_year += 1
                continue
            elif prayer.timestamp.astimezone(timezone('US/Central')).strftime('%Y-%m') == month:
                prayed_for_month += 1
                prayed_for_year += 1
                continue
            elif prayer.timestamp.astimezone(timezone('US/Central')).strftime('%Y') == year:
                prayed_for_year += 1
        return render_to_response('mypraylist.html', {'today': today, 'user':request.user, 'top_groups': top_groups, 'saved_groups': saved_groups, 'saved_prayers': allprayers, 'prayed_today': prayed_today, 'form': form, 'userprayers': custom_prayers, 'prayed_for_today': prayed_for_today, 'prayed_for_month': prayed_for_month, 'prayed_for_year': prayed_for_year}, context_instance=RequestContext(request))

def mypraylist_check(request, postid):
    if request.is_ajax():
        if "c" in postid:
            custom_p = SavedPrayerCustom.objects.get(id=postid[1:])
            userobj = User.objects.get(username=request.user)
            dt = datetime.datetime.now()
            dtclean = dt.strftime('%Y-%m-%d %H:%M:%S')     
            new_p = PrayedFor(prayed_user=userobj, timestamp=dtclean, prayer_custom=custom_p)
            new_p.save()
            return HttpResponse(200)
        else:
            prayer = Prayer.objects.get(id=postid)    
            userobj = User.objects.get(username=request.user)
            dt = datetime.datetime.now()
            dtclean = dt.strftime('%Y-%m-%d %H:%M:%S')     
            new_p = PrayedFor(prayed_user=userobj, timestamp=dtclean, prayer=prayer)
            new_p.save()
            return HttpResponse(200)

def delete_daily(request, postid):
    if "c" in postid:
        custom_p = SavedPrayerCustom.objects.get(id=postid[1:])
        custom_p.delete()
        return HttpResponse(200)
    else:
        userobj = User.objects.get(username=request.user)
        prayer = Prayer.objects.get(id=postid)
        userobj.profile.saved_prayer.remove(prayer)
        return HttpResponse(200)

