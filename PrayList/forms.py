from django import forms

class PrayerForm(forms.Form):
    subject = forms.CharField(max_length=150)
    prayer = forms.CharField(widget=forms.Textarea)
    group = forms.CharField(max_length=30)

class GroupForm(forms.Form):
    options = ((0, 'public'), (1, 'private'))
    privacy = forms.TypedChoiceField(
            choices=options, widget=forms.RadioSelect, coerce=int
        )