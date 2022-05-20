from django.urls import path

from .views import se, twitter_login, twitter_callback, twitter_logout

urlpatterns = [
    path('fff/', se, name='defef'),
    path('twitter_login/', twitter_login, name='twitter_login'),
    path('twitter_callback/', twitter_callback, name='twitter_callback'),
    path('twitter_logout/', twitter_logout, name='twitter_logout'),
]