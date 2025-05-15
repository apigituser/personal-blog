from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')

def add_article(request):
    return render(request, 'post.html')