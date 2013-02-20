from forms import PrayerForm
from models import Prayer
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect

def submit(request):
	if request.method == "POST":
		form = PrayerForm(request.POST)
		if form.is_valid():
		#	return HttpResponseRedirect('/submit/thanks/')
			p= Prayer(subject = request.POST['subject'], prayer = request.POST['prayer'])
			p.save()
	else:
		form = PrayerForm()
	return render_to_response('submit.html', {'form': form})

def new(request):
	obj_list = Prayer.objects.all()
	return render_to_response('new.html', {'prayers': obj_list})