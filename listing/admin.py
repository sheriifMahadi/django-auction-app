from django.contrib import admin

from .models import Category, Listing, ListingBid

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['item', 'created_by', 'slug', 
                    'price', 'is_active', 'date_created',
                    ]
    list_filter = ['is_active']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('item', )}


@admin.register(ListingBid)
class ListingBidAdmin(admin.ModelAdmin):
    list_display = ['item', 'bids', ]

