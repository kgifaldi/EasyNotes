from django import forms

class userForm(forms.Form):
    htmlusername = forms.CharField(max_length=200)
    htmlpassword = forms.CharField(max_length=200)

class classForm(forms.Form):
    htmlClassName = forms.CharField(max_length=200)
    htmlday = forms.MultipleChoiceField()
    htmlStartTime = forms.TimeField()
    htmlEndTime = forms.TimeField()
