import django_filters
from listings.models import Listing

class ListingFilter(django_filters.FilterSet):

    class Meta:
        model= Listing
        fields={
            # 'keywords':['icontains'],
            'city':['iexact'],
            'state':['iexact'],
            'bedrooms':['lte'],
            'price':['lte'],

        }