from django.shortcuts import render
from django.http import HttpResponse
from .forms import Article
import json, datetime, os

def article(request, id):
    files = os.listdir("./articles/")

    for file in files:
        if file.startswith(str(id)):
            with open(f'./articles/{file}') as f:
                data = json.load(f)
                return render(request, 'article.html', context={'payload': data})
    return HttpResponse('Something went wrong')

def home(request):
    articles = list()
    files = os.listdir("./articles/")

    for file in files:
        with open(f'./articles/{file}') as f:
            data = json.load(f)
            articles.append(data)
    return render(request, 'home.html', context={'payload': articles})

def new(request):
    files = os.listdir("./articles/")

    if request.method == "POST":
        form = Article(request.POST)

        if form.is_valid():
            date = datetime.datetime.now().strftime("%d/%m/%Y")
            id = len(files) + 1
            article = {id: form.cleaned_data}
            article[id].update({'published': date})

            title = form.cleaned_data.get("title")
            filename = f'./articles/{id}_{title}.json'
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            with open(filename, 'w') as file:
                json.dump(article, file)
            
            return render(request, 'post.html')
        return HttpResponse('Form Invalid: Sowry :)')
    else:
        return render(request, 'new.html')