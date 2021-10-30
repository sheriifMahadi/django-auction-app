from django.urls import path

from . import views


app_name = 'listing'

urlpatterns = [
    path('', views.listings, name='listings'),
    path('category/<slug:slug>', views.category_list, name='category_list'), 
    path('item/<slug:slug>', views.item_detail, name='item_detail')

]

