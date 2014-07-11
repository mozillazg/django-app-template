#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django import forms

from .models import Poll


class CreateForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ()
