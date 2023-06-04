from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name = 'Login'),
    path('logout', views.Logout, name = 'Logout'),
    path('register', views.register, name='register'),
    path('home', views.home, name = 'home'),
    path('close', views.close_month, name = 'close_month'),
    path('insert', views.insert, name = 'Insert'),
    path('list', views.RecordIndexView.as_view(), name = 'List'),
    path('<int:record_id>/detail/', views.detail_view, name = 'detail_view'),
    path('<int:record_id>/edit/', views.edit_view, name = 'edit_view'),
    path('<int:pk>/delete/', views.RecordDeleteView.as_view(), name = 'Delete'),
    path('import', views.csvimport, name = 'csvimport'),
    path('export', views.csvexport, name = 'csvexport'),
]

