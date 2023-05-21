from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name = 'Login'),
    path('logout', views.Logout, name = 'Logout'),
    path('register', views.Register, name='register'),
    path('home', views.home, name = 'home'),
]

