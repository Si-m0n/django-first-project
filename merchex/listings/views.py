from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm

# Create your views here.
def band_list(request):
    band = Band.objects.all()
    return render(
        request,
        "listings/band_list.html",
        {"bands": band},
    )


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(
        request,
        "listings/band_detail.html",
        {"band": band},
    )


def about(request):
    return render(request, "listings/about.html")


def listings_list(request):
    listings = Listing.objects.all()
    return render(
        request,
        "listings/listings_list.html",
        {
            "listings": listings,
        },
    )


def listings_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(
        request,
        "listings/listings_detail.html",
        {"listing": listing},
    )


def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex Contact Us form',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
            return redirect("email-sent")
    else:
        form = ContactUsForm()
    return render(
        request,
        "listings/contact.html",
        {"form": form},
    )


def email_sent(request):
    return render(request, "listings/email_sent.html")
