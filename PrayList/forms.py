from django import forms
from tagging.forms import TagField

class PrayerForm(forms.Form):
    subject = forms.CharField(max_length=150)
    prayer = forms.CharField(widget=forms.Textarea)
    tags = TagField()