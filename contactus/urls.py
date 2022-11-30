from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from contactus import views

urlpatterns = [
    path('', views.gallery, name='contactus'),
]
