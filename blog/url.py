from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('music/', views.music,  name='blog-music')
]

