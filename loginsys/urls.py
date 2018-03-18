from django.urls import path, include
from . import views

app_name = 'loginsys'
urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register/', views.register, name='register'),
]
