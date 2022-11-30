from django.shortcuts import render, HttpResponse
import json
import os
# Create your views here.


def cars(request, car):
    context = {
        "title": "Cars-WeddingCarRide",
        "car": car.capitalize(),
        "imgs": os.listdir(f'static/images/cars/{car}'),
        "name": car,
    }
    
    return render(request, "cars/home.html", context=context)
