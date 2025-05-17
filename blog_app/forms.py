from django import forms

class Article(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=1000)

class Login(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)