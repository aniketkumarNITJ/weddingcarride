from django.shortcuts import render, HttpResponse
import json
# Create your views here.


def home(request):
    context = {
        "title": "Tours-WeddingCarRide"
    }
    return render(request, "tours/home.html", context=context)
