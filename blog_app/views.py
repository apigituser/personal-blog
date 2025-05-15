from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def new(request):
    if request.method == "POST":
        return render(request, 'post.html')
    else:
        return render(request, 'new.html')