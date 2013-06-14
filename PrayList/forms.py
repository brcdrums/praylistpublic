from django import forms

class PrayerForm(forms.Form):
    subject = forms.CharField(max_length=150)
    prayer = forms.CharField(widget=forms.Textarea)
    prayer_group = forms.CharField(max_length=30)

class GroupForm(forms.Form):
    group = forms.CharField(max_length=30)
    options = ((0, 'public'), (1, 'private'))
    privacy = forms.TypedChoiceField(
            choices=options, widget=forms.RadioSelect, coerce=int
        )

class NewCustomPrayer(forms.Form):
    newprayer = forms.CharField(max_length=50)

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40}), max_length=2000)