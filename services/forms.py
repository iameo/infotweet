from email.policy import default
from secrets import choice
from typing import ForwardRef
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset

class SearchForm(forms.Form):
    distance_kms = [
        ("1km", "1KM"),
        ("5km", "<5KM"),
        ("10km", "<10KM"),
        ("20km", "<20KM"),
        ("40km", "<40KM"),
        ("100km", "<100KM"),
        ("1000km", ">500KM"),
        ("5000km", ">1000KM")
    ]

    result_types = [
        ("mixed", "Popular + Real-time"),
        ("recent", "Only Recent tweets"),
        ("popular", "Most Popular")
    ]

    keyword = forms.CharField(label='keyword', max_length=500, widget=forms.TextInput(attrs={'placeholder':'enter query (ex: doughnut)'})) #q
    distance = forms.ChoiceField(label='geocode', choices=distance_kms, disabled=True)
    langauge = forms.CharField(label='language', max_length=4, widget=forms.TextInput(attrs={'placeholder':'en', 'value': 'en'}))
    type = forms.ChoiceField(label='result type', choices=result_types)
    current_location = forms.BooleanField(label='use current location', required=False)
    

class ActivityForm(forms.Form):
    like_ = [
        ('all', 'ALL'),
        ('30%', '30%')
    ]

    follow_ = [
        ('all', 'ALL'),
        ('50%', '50%'),
        ('70%', '70%')
    ]

    favorite = forms.ChoiceField(label="like schema", choices=like_, required=False)
    follow = forms.ChoiceField(label='follow schema', choices=follow_, required=False)