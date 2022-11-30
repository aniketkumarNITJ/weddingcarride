from django.shortcuts import render, HttpResponse
import json
# Create your views here.


def aboutus(request):
    context = {
        "title": "AboutUS-WeddingCarRide"
    }
    return render(request, "aboutus/home.html", context=context)
