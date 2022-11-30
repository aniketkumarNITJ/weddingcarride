from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from cars import views

urlpatterns = [
    path('<str:car>/', views.cars, name='cars'),
]
