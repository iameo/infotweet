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
    latlng, city = g.latlng, g.city
    geocode_ = f'{latlng[0]},{latlng[1]},{distance}'
    return geocode_, city
