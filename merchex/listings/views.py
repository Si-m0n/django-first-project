from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band
from listings.models import Listing

# Create your views here.
def hello(request):
    band = Band.objects.all()
    return HttpResponse(
        f"""<h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :</p>
        <ul>
            <li>{band[0].name}</li>
            <li>{band[1].name}</li>
            <li>{band[2].name}</li>
        </ul>
    """
    )


def about(request):
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons merch !</p>")


def listings(request):
    listing = Listing.objects.all()
    return HttpResponse(
        f"""<h1>Listings</h1>
        <ul>
            <li>{listing[0].title}</li>
            <li>{listing[1].title}</li>
            <li>{listing[2].title}</li>
            <li>{listing[3].title}</li>
    """
    )


def contact(request):
    return HttpResponse("<h1>Nous contacter :</h1> <p>Téléphone : 06 ** ** ** ** </p>")
