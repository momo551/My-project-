from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
]

    #path('users/', views.user_list, name='user_list'),