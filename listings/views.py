from django.shortcuts import render
from .models import Listings


def index(request):
    return render(request, 'listings/index.html')

def all_listings(request):
    all_listings = Listings.objects.order_by('-list_date')
    context = {'all_listings': all_listings}
    return render(request, 'listings/all_listings.html', context)

