from curses import noecho
from django.shortcuts import render, get_object_or_404

from .models import Category, Listing, ListingBid
from userBids.models import WatchList

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def listings(request):
    top_listings = Listing.listings.all()[:4]

    # display new items
    new_listings = Listing.listings.all()[4:]

    context = {'top_listings': top_listings, 'new_listings': new_listings}
    return render(request, 'listing/home.html',context)


def item_detail(request, slug):
    listing = get_object_or_404(Listing, slug=slug, is_active=True)
    bids = ListingBid.objects.filter(item=listing.id).values('bids')
    user_item = WatchList.objects.filter(user=request.user)
    watch_item = user_item[0].item.filter(item=listing)    
    bidCount = ListingBid.objects.filter(item=listing.id).first()
    if bidCount:
        bidCount = bidCount.bidders.count()
    else:
        bidCount = 0

    context = {'listing': listing,  
    'watchlist_item': watch_item,
    'bids': bidCount
    }
    return render(request, 'listing/items/item_detail.html', context)

def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    listings = Listing.objects.filter(category=category)
    context = {'category': category, 'listings': listings}
    return render(request, 'listing/categories.html', context)
    


