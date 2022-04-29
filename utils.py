from datetime import datetime

def tweet_source(source):
    source = source.lower()
    if 'iphone' in source:
        return 'apple'
    if 'android' in source:
        return 'android'
    if 'web' in source:
        return 'browser' 
    else:
        return 'circle-question'

def tweet_location(location):
    if location:
        if len(location) > 13:
            return str(location[:13]) + '..'
        return location
    return 'Nil'

def check_verification(verify):
    if verify is True:
        return 'badge-check'
    return verify

def check_contributors_status(contributor_bool):
    if contributor_bool is True:
        return 'money-bill'
    return ''

def calculate_profile_age(start_date):
    """a generic function that returns a profile's age"""
    today = datetime.today()
    profile_age = today - start_date.replace(tzinfo=None) 
    return profile_age.days
