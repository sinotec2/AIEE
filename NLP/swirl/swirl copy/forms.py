'''
@author:     Sid Probstein
@contact:    sid@swirl.today
'''

from sys import path
from os import environ
import logging as logger
logger.basicConfig(level=logger.INFO)
from datetime import timedelta

import django
from django.utils import timezone

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from swirl.models import QueryTransform

from swirl.utils import swirl_setdir
path.append(swirl_setdir()) # path to settings.py file
environ.setdefault('DJANGO_SETTINGS_MODULE', 'swirl_server.settings')
django.setup()

module_name = 'forms.py'

##################################################
##################################################

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
            user = super().save(commit=False)
            user.username = self.cleaned_data['email']
            if commit:
                user.save()
            return user

##################################################

class SearchForm(forms.Form):
    q = forms.CharField()
    search_id = forms.IntegerField(required=False)

class QueryTransformForm(forms.Form):
    file = forms.FileField(label='CSV Filename')
    name = forms.CharField(max_length=255, required=False, label='Name')
    content_type = forms.ChoiceField(choices=QueryTransform.QUERY_TRASNSFORM_TYPE_CHOICES, label='Type')
