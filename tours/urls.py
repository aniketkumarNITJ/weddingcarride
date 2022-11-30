from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from tours import views

urlpatterns = [
    path('', views.home, name='tours'),
]
