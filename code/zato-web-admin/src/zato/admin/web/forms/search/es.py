# -*- coding: utf-8 -*-

"""
Copyright (C) 2014 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# Django
from django import forms

# elasticutils
from elasticutils import DEFAULT_TIMEOUT

# Zato
from zato.common import SEARCH

class CreateForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'required', 'style':'width:100%'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'checked':'checked'}))
    hosts = forms.CharField(
        initial=SEARCH.ES.DEFAULTS.HOSTS.value, widget=forms.Textarea(attrs={'style':'width:100%', 'class':'required'}))
    timeout = forms.CharField(initial=DEFAULT_TIMEOUT, widget=forms.TextInput(attrs={'class':'required', 'style':'width:15%'}))
    body_as = forms.CharField(initial=SEARCH.ES.DEFAULTS.BODY_AS.value,
        widget=forms.TextInput(attrs={'class':'required', 'style':'width:15%'}))

class EditForm(CreateForm):
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput())
