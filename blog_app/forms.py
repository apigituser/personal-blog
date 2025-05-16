from django import forms

class Article(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=1000)