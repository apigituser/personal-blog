from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('new/', views.new),
    path('add-article/', views.add_article),
]

'''
[ENDPOINTS]
    Guest Section
    	/home -> list of articles published on the blog
    	/article/{id} -> article
    Admin Section
    	/admin -> add,edit,delete articles
    	/edit/{id} -> edit article
    	/new -> add new article
'''