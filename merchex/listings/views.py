from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello Django !</h1>")


def about(request):
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons merch !</p>")


def listings(request):
    return HttpResponse("<h1>Listings</h1>")


def contact(request):
    return HttpResponse("<h1>Nous contacter :</h1> <p>Téléphone : 06 ** ** ** ** </p>")
