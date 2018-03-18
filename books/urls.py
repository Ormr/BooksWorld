"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:author_id>/', views.detail, name='detail'),
    path('<int:author_id>/<int:book_id>/', views.description, name='description'),
    path('all_books/', views.all_books, name='all_books'),
    path('search/', views.search, name='search'),
    path('<int:author_id>/<int:book_id>/add_comment/', views.add_comment, name='add_comment'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_books/', views.add_books, name='add_books'),
]
