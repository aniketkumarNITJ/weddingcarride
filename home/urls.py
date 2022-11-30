from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('yandex_f38cd84aed5201d8.html', views.yandex, name='yandex'),
]
