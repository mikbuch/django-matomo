Django-Matomo
=============

A simple app to add the Matomo JS tracking code to your template.

``django-matomo`` is listed as an official Django integration package at: https://matomo.org/integrate/  (since April 2022).

The current repository has been forked from `django-piwik <https://github.com/jasjukaitis/django-piwik>`_ (legacy) by Raphael "`jasjukaitis <https://github.com/jasjukaitis>`_" Jasjukaitis. ``django-piwik`` was listed as an official Django plugin for Matomo from 2013 to March 2022.

Requirements
------------

* Django
* A running Matomo analytics server


Installation
------------

Using PyPI you can simply type into a terminal:

``pip install django-matomo``

(the suggested way)

or

``easy_install django-matomo``


Configuration
-------------

Add ``matomo`` to the list of ``INSTALLED_APPS`` in your ``settings.py`` file, i.e.:

..  code-block:: python

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'matomo',
    ]

You also need to add ``MATOMO_SITE_ID`` (e.g. `51`) and ``MATOMO_URL`` (e.g. ``'http://matomo.example.com/'``, please don't forget the trailing slash!) to your ``settings.py file`` -- these are required. E.g.:

..  code-block:: python

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'matomo',
    ]
    
    # Matomo tracking server and site information
    MATOMO_URL = "https://matomo.example.com/"
    MATOMO_SITE_ID = 51

You can get ``MATOMO_SITE_ID`` and ``MATOMO_URL`` from the administrator of your Matomo server.

In the template, put ``{% load matomo_tags %}`` at the top, and add ``{% tracking_code %}`` before the ``</body>`` tag.

That's it. Happy tracking!

Uploading to PyPi
-----------------

Article on Medium (Towards Data Science) on `how to upload packages to PyPi <https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3>`_.

In short:

``python setup.py sdist``

``twine upload dist/*``

Version history
---------------

* Version ``0.1.6`` README changes after accepting ``django-matomo`` as an official Matomo plugin.

* Version ``0.1.5`` information on uploading to PyPi added to the README. Minor formatting changes.

* Versions up to ``0.1.4`` are mainly formatting changes for the RST README format.

* Main changes were introduced in ``0.1`` version of the package.


Author(s)
---------

Copyright 2022 Mikolaj Buchwald <mikolaj.buchwald@gmail.com>

as ``django-piwik``: Copyright 2013 Raphael Jasjukaitis <webmaster@raphaa.de>


Released under the BSD license.
