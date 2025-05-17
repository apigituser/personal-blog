from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin),
    path('home/', views.home),
    path('new/', views.new),
    path('article/<int:id>', views.article),
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