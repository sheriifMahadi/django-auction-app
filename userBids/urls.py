from django.urls import path

from . import views

app_name = 'my_bids'

urlpatterns = [
    path("bids/", views.my_bids, name='my-bids'),
    path("bid/<str:item>/", views.bid_on_item, name='bid_on_item'),
    path("rm_bid/<str:item>/", views.remove_from_bids, name='rm_bids'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path("logout/", views.logout_request, name= 'logout'),
    path("watchlist", views.watchlist, name='watchlist'),
    path("watch/<str:item>/", views.add_to_watchlist, name='add_watchlist'),
    path("rm_watch/<str:item>/", views.remove_watchlist_item, name='rm_watchlist')
]
