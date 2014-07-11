#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
#
#
# @python_2_unicode_compatible
# class Poll(models.Model):
#     name = models.CharField(_('name'), max_length=100)
#
#     class Meta:
#         verbose_name = _('poll')
#         verbose_name_plural = _('polls')
#
#     def __str__(self):
#         return self.name
