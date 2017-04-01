from django import forms

class userForm(forms.Form):
    htmlusername = forms.CharField(max_length=200)
    htmlpassword = forms.CharField(max_length=200)
