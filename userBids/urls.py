from django.urls import path

from . import views

app_name = 'my_bids'

urlpatterns = [
    path('my_bids', views.my_bids, name='my-bids'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("watchlist", views.watchlist, name='watchlist'),
    path("watch/<str:item>", views.add_to_watchlist, name='add_watchlist'),
    path("rm_watch/<str:item>", views.remove_watchlist_item, name='rm_watchlist')

]
