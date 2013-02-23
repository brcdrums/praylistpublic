from django import forms

class PrayerForm(forms.Form):
	subject = forms.CharField(max_length=150)
	prayer = forms.CharField(widget=forms.Textarea)
