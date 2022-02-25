from django.shortcuts import render

# Create your views here.
def listings(request):
    return render(request,'listings/listings.html')

def listdetail(request, pk):
    return render(request,'listings/listdetail.html')

def search(request):
    return render(request, 'listings/search.html')
