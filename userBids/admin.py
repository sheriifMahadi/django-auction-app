from django.contrib import admin

from .models import WatchList, UserBids
admin.site.register(WatchList)
admin.site.register(UserBids)