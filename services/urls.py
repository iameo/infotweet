
from django.urls import path

from .views import home_view, search_tweets, ff, getClient
  
urlpatterns = [
    path('', home_view, name='home-view'),
    path('search/', search_tweets, name='search_tweets'),
    path('abc/', ff, name='ab'),
    path('f/', getClient, name='authf')
]