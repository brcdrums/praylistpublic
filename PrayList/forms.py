from django import forms

class PrayerForm(forms.Form):
	subject = forms.CharField(max_length=50)
	prayer = forms.CharField(widget=forms.Textarea)
