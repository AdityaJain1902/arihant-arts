from django.shortcuts import render, redirect
from .models import Artwork, Enquiry

def collection(request):
    artworks = Artwork.objects.filter(is_available=True)
    return render(request, "collection.html", {"artworks": artworks})


def create_enquiry(request, art_id):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")

        artwork = Artwork.objects.get(id=art_id)

        Enquiry.objects.create(
            customer_name=name,
            phone_number=phone,
            artwork=artwork
        )

    return redirect('collection')
