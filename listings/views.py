from django.shortcuts import render,redirect
from .models import Listings
from .forms import ListingForm


def index(request):
    return render(request, 'listings/index.html')

def all_listings(request):
    all_listings = Listings.objects.order_by('-list_date')
    context = {'all_listings': all_listings}
    return render(request, 'listings/all_listings.html', context)

def new_listing(request):
    if request.method != 'POST':
        form = ListingForm()
    else:
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listings:all_listings')
      
    context = {'form': form}
    return render(request, 'listings/new_listing.html', context)

def detail(request,detail_id):
    detail = Listings.objects.get(id=detail_id)
    context = {'detail':detail}
    return render(request, 'listings/detail.html', context)