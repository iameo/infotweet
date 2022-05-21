
from django.urls import path

from .views import home_view, search_tweets, ff
  
urlpatterns = [
    path('', home_view, name='home-view'),
    path('search/', search_tweets, name='search_tweets'),
    path('welcome/', ff, name='welcome'),
]