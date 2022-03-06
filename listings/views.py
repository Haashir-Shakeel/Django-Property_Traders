from django.shortcuts import get_object_or_404, render
from listings.models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from listings.choices import state_choices,price_choices,bedroom_choices
from listings.filters import ListingFilter

# Create your views here.
def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context = {
        'listings':paged_listings
    }

    return render(request,'listings/listings.html',context)

def listdetail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context={
        'listing':listing
    }

    return render(request,'listings/listdetail.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    
    # f = ListingFilter(request.GET, queryset=Listing.objects.all())
    # queryset_list=f.qs

    context={
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        # 'filter': f,
        'values':request.GET,
    }
    return render(request, 'listings/search.html',context)
