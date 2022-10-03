from django.shortcuts import render
from .models import *

# -------------------------------- Главная страница --------------------------------
def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})

def plants(request):
    plants = Plants.objects.all()
    return render(request, 'main/plants.html', {"plants": plants})


def forPlants(request):
    allFor = ForPlants.objects.all()
    return render(request, 'main/forPlants.html', {'allFor': allFor})


def oceanTheme(request):
    ocean = OceanTheme.objects.all()
    return render(request, 'main/oceanTheme.html', {'ocean': ocean})


def help(request):
    return render(request, 'main/help.html', {'title': 'Помощь'})


