from django.shortcuts import render, HttpResponse
import json
# Create your views here.


def home(request):
    context = {
        "title": "Home-WeddingCarRide"
    }
    return render(request, "home/home.html", context=context)

def yandex(request):
    return render(request, "home/yandex.html")
