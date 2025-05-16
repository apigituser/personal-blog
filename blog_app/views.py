from django.shortcuts import render
from django.http import HttpResponse
from .forms import Article
import json, datetime, os

def home(request):
    return render(request, 'home.html')

def new(request):
    if request.method == "POST":
        form = Article(request.POST)

        if form.is_valid():
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            payload = form.cleaned_data
            title = form.cleaned_data.get("title")
            payload.update({'published': date})

            filename = f'./articles/{title}.json'
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(filename, 'w') as file:
                json.dump(payload, file)
            
            return render(request, 'post.html')
        return HttpResponse('Form Invalid: Sowry :)')
    else:
        return render(request, 'new.html')