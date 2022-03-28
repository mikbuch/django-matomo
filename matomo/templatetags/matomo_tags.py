# -*- coding: utf-8 -*-
"""Matomo template tag."""

from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


register = template.Library()


@register.inclusion_tag('matomo/tracking_code.html')
def tracking_code():
    try:
        id = settings.MATOMO_SITE_ID
    except AttributeError:
        raise ImproperlyConfigured('MATOMO_SITE_ID does not exist.')
    try:
        url = settings.MATOMO_URL
    except AttributeError:
        raise ImproperlyConfigured('MATOMO_URL does not exist.')
    return {'id': id, 'url': url}
