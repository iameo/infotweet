from django.shortcuts import render
from requests import request
from .forms import SearchForm, ActivityForm
import tweepy
  
from utils import tweet_source, tweet_location, check_verification, check_contributors_status, calculate_profile_age, retrieve_original_dp, fetch_search
from django.core.paginator import Paginator

# from twython import Twython

from django.http import HttpResponseRedirect
from django.urls import reverse
import requests
from socialauth.wrapper import twitter_login_required
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import os

from socialauth.api import TwitterAPI
from socialauth.models import TwitterUser


def getClient(request):
    user = TwitterUser.objects.filter(user=request.user)
    try:
        client = tweepy.Client(consumer_key=self.api_key, consumer_secret=self.api_secret, access_token=user.twitter_oauth_token.oauth_token,
                                access_token_secret=user.twitter_oauth_token.oauth_token_secret, wait_on_rate_limit=True)
    except Exception as e:
        return None
    return client



def social_home(request):
    return render(request, "abc.html")

@login_required
@twitter_login_required
def home_view(request):
    context = {}
    context['form'] = SearchForm()
    return render( request, "home.html", context)


def search_tweets(request):
    twitter = TwitterAPI()
    # client = request.session['clientele']
    user = TwitterUser.objects.filter(user=request.user).first()
    client = tweepy.Client(consumer_key=twitter.api_key, consumer_secret=twitter.api_secret, access_token=user.twitter_oauth_token.oauth_token,
                                access_token_secret=user.twitter_oauth_token.oauth_token_secret, wait_on_rate_limit=True)
    # getClient(request)

    params = {}
    data = []

    params['q'] = request.GET.get('keyword')
    params['geocode'] = request.GET.get('distance')
    params['lang'] = request.GET.get('language')
    params['result_type'] = request.GET.get('type')
    params['current_location'] = request.GET.get('current_location')

    
    results, city = fetch_search(params, exclude_q_in_name=False, client=client)


    dp_links = [retrieve_original_dp(l.user.profile_image_url_https) for l in results]
    screen_names = [l.user.screen_name for l in results]
    names = [l.user.name for l in results]
    locations = [tweet_location(l.user.location) for l in results]
    tweets = [l.text for l in results]
    ff_counts = [l.user.friends_count for l in results]
    flr_counts = [l.user.followers_count for l in results]
    verified = [check_verification(l.user.verified) for l in results]
    contributors = [check_contributors_status(l.user.contributors_enabled) for l in results]
    rt_counts = [l.retweet_count for l in results]
    favs_counts = [l.favorite_count for l in results]
    sources = [tweet_source(l.source) for l in results]
    user_created_dates = [calculate_profile_age(l.user.created_at) for l in results]
    tweet_created_dates = [l.created_at for l in results]
    quotables = [l.is_quote_status for l in results]
    replies = [l.in_reply_to_screen_name for l in results]
    # reply_counts = [l.reply_count for l in results]

    iterable_ = list(
                    zip(screen_names,names, tweets, locations, verified, ff_counts, flr_counts, \
                        contributors, rt_counts, user_created_dates, dp_links, sources, tweet_created_dates, replies, quotables, favs_counts
                    )
                )

    [data.append(dict(
            screen_name=iter_[0], 
            name=iter_[1],
            tweet=iter_[2], 
            location=iter_[3],
            verified=iter_[4], 
            followers_count=iter_[5],
            friends_count=iter_[6], 
            contributors_enabled=iter_[7],
            retweet_count=iter_[8], 
            user_created_at=iter_[9],
            dp_link=iter_[10],
            source=iter_[11],
            tweet_created_at=iter_[12],
            is_reply=iter_[13],
            is_quote=iter_[14],
            fav_count=iter_[15],
            # reply_count=iter_[16]
            )) for iter_ in iterable_]

    # paginator = Paginator(data, per_page=10)
    # page_object = paginator.get_page(page)
    # context = {"page_obj":page_object, "city":city}
    context = {"data": data, "city": city, "keyword": params['q'], "activity_form": ActivityForm()}
    # if context:
    #     render(request, 'results.html', context)

    if request.htmx:
        return render(request,'results.html', context)
    return render(request,'results.html', context)



def create_fav(request):
    client = getClient()
     
    status_list = []
    for status in status_list:
        client.create_favorite(status.id, include_entities=True)


def ff(request):
    return render(request, 'abc.html')

# @app.route('/twitter')
# def access():
#     try:
#         if not twitter.authorized:
#             return redirect(url_for("twitter.login"))
#     except Exception as e:
#         print(e)
#     else:
#         resp = twitter.get('account/settings.json')
#         assert resp.ok
#         return redirect(url_for('home'))
