from forms import PrayerForm
from models import Prayer
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
import datetime

def submit(request):
	if request.method == "POST":
		form = PrayerForm(request.POST)
		if form.is_valid():
			dt = datetime.datetime.now()
			dtclean = dt.strftime('%Y-%m-%d %H:%M:%S')
		#	return HttpResponseRedirect('/submit/thanks/')
			p= Prayer(subject = request.POST['subject'], prayer = request.POST['prayer'], timestamp=dtclean)
			p.save()
	else:
		form = PrayerForm()
	return render_to_response('submit.html', {'form': form})

def new(request):
	obj_list = Prayer.objects.order_by("-id")
	return render_to_response('new.html', {'prayers': obj_list})