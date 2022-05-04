from datetime import datetime

def tweet_source(source):
    source = source.lower()
    if 'iphone' in source:
        return 'apple'
    if 'android' in source:
        return 'android'
    if 'web' in source:
        return 'desktop' 
    else:
        return 'circle-question'


def tweet_location(location):
    return str(location) if len(location) > 1 else 'Nil'


def check_verification(verify):
    if verify is True:
        return 'circle-check'
    return verify


def check_contributors_status(contributor_bool):
    if contributor_bool is True:
        return 'money-bill-wave'
    return ''


def calculate_profile_age(start_date):
    """a generic function that returns a profile's age"""
    today = datetime.today()
    profile_age = today - start_date.replace(tzinfo=None) 
    return profile_age.days


def retrieve_original_dp(link):
    return link.replace('_normal', '')


def fetch_geolocation(distance):
    import geocoder
    g = geocoder.ip('me')
    try:
        lat, lng, city = g.latlng[0], g.latlng[1], g.city
    except Exception as e:
        return '', 'Could not ascertain'
    geocode_ = f'{lat},{lng},{distance}'
    return geocode_, city


def fetch_search(params, exclude_q_in_name=False, client=None):
    city = 'Worldwide'
    if params['current_location']:
        geocode_, city = fetch_geolocation(params['geocode'])
        results = client.search_tweets(
            q=params['q'], geocode=str(geocode_), lang=params['lang'], result_type=params['result_type'], count=60
            )
    else:
        results = client.search_tweets(
            q=params['q'], lang=params['lang'], result_type=params['result_type'], count=60
        )

    if exclude_q_in_name:
        results = [data for data in results if params['q'] not in data.user.screen_name]
        return results, city
    return results, city