from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from gallery import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
]
