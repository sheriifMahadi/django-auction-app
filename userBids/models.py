from django.db import models
from django.contrib.auth.models import User

from listing.models import Listing

class UserBids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name='bidding_user')
    item = models.ManyToManyField(Listing,
    related_name='user_item')

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_watchlist')
    item = models.ManyToManyField(Listing, related_name='item_sin_the_watchlist', blank=True)

    def __str__(self):
        return f'{self.user} watchlist'