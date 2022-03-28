Django-Matomo
============

A simple app to add the Matomo JS tracking code to your template.

Forked from [django-piwik](https://github.com/jasjukaitis/django-piwik) (legacy) by Raphael Jasjukaitis [jasjukaitis](https://github.com/jasjukaitis).

`django-piwik` is metioned as an official Django plugin for Matomo: https://matomo.org/integrate/

Requirements
------------

* Django


Installation
------------

Using PyPI you can simply type into a terminal:

    pip install django-matomo

or

    easy_install django-matomo


Configuration
-------------

Add ``matomo`` to the list of ``INSTALLED_APPS`` in your ``settings.py`` file.

Also ``MATOMO_SITE_ID`` (e.g. ``51``) and ``MATOMO_URL`` (e.g. ``'http://matomo.example.com/'``, please don't forget the trailing slash!) are required.


In the template, put ``{% load piwik_tags %}`` to the top and add ``{% tracking_code %}`` before the ``</body>`` tag.


That's it. Happy tracking!


Author
------

Copyright 2022 Mikolaj Buchwald <mikolaj.buchwald@gmail.com>

as `django-piwik`: Copyright 2013 Raphael Jasjukaitis <webmaster@raphaa.de>


Released under the BSD license.
