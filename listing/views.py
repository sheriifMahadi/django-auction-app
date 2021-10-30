from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Listing

def categories(request):
    return {
        'categories': Category.objects.all()
    }


def listings(request):
    top_listings = Listing.objects.all()[:4]

    # display new items
    new_listings = Listing.objects.all()[4:]

    context = {'top_listings': top_listings, 'new_listings': new_listings}
    return render(request, 'listing/home.html',context)


def item_detail(request, slug):
    listing = get_object_or_404(Listing, slug=slug, is_active=True)
    context = {'listing': listing}
    return render(request, 'listing/items/item_detail.html', context)


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    listings = Listing.objects.filter(category=category)
    context = {'category': category, 'listings': listings}
    return render(request, 'listing/categories.html', context)
    
    
    

"""#TODO:Write custom query to return active listings
and ones that havent been auctioned yet, 
show 12 products on home page, 3 each from different
categories."""
