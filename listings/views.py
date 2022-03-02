from django.shortcuts import render
from listings.models import Listing

# Create your views here.
def listings(request):
    listings = Listing.objects.all()

    context = {
        'listings':listings
    }

    return render(request,'listings/listings.html',context)

def listdetail(request, listing_id):
    return render(request,'listings/listdetail.html')

def search(request):
    return render(request, 'listings/search.html')
