# Views for App here
from django.http import request
from django.shortcuts import render


def view_home_page(request):
    return render(request, 'baseTemplate.html')

def get_home_page(request):
    return render(request, 'homePage.html')

def get_furniture_page(request):
    return render(request, "furniturePage.html")