from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from listing.models import Listing, ListingBid

from .forms import NewUserForm
from .models import WatchList, UserBids

@login_required
def my_bids(request):
	bids = ListingBid.objects.filter(bidders=request.user).values('item_id')
	item = Listing.objects.filter(id__in = bids)
	total = 0
	for i in item:
		total += i.price
	context = {'bids': item, 'total': total}
	return render(request, 'listing/userbids/my_bids.html', context)

def bid_on_item(request, item):
	user = request.user
	get_item = get_object_or_404(Listing, slug=item)
	user_bids = UserBids.objects.filter(user=user)
	check = ListingBid.objects.filter(item=get_item.id)
	if check:
		newListingBid = ListingBid.objects.get(item=get_item.id)
		newListingBid.bidders.add(user)
	else:
		newListingBid= ListingBid.objects.create(item=get_item)
		newListingBid.bidders.add(user)

	if user_bids:
		new = UserBids.objects.get(user=user)
		new.item.add(get_item)
	else:
		new = UserBids.objects.create(user=user)
		new.item.add(get_item)

	return HttpResponseRedirect(reverse('my_bids:my-bids'))

def remove_from_bids(request, item):
	listing = get_object_or_404(Listing, slug=item)
	user_bid = UserBids.objects.filter(user=request.user).first()
	user_bid.item.remove(listing)
	bid_item= ListingBid.objects.filter(bidders=request.user).first()
	bid_item.bidders.remove(request.user)
	return HttpResponseRedirect(reverse('my_bids:my-bids'))

@login_required
def add_to_watchlist(request, item):
	get_item = Listing.objects.get(item=item)
	user = request.user
	watch_user = WatchList.objects.filter(user=user)
	if watch_user:
		create = WatchList.objects.get(user = request.user)
		create.item.add(get_item)
	else:
		create = WatchList.objects.create(user=user)
		create.item.add(get_item)
	return HttpResponseRedirect(reverse('my_bids:watchlist'))

@login_required
def watchlist(request):
	user_name = request.user
	user_item = WatchList.objects.filter(user=request.user).values('item')
	item = Listing.objects.filter(id__in = user_item)
	context = {'watchlist': item, 'user': user_name}
	return render(request, 'listing/userbids/watch_list.html', context)

@login_required
def remove_watchlist_item(request, item):
	listing = get_object_or_404(Listing, slug=item)
	user_item = WatchList.objects.filter(user=request.user)
	user_item[0].item.remove(listing)
	return HttpResponseRedirect(reverse('my_bids:watchlist'))

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("listing:listings")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="listing/userbids/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("listing:listings")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="listing/userbids/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("listing:listings")


#TODO: Implement live search using JS filter. then host the app on pythonanywhere