Django-Matomo
=============

A simple app to add the Matomo JS tracking code to your template.

Forked from `django-piwik <https://github.com/jasjukaitis/django-piwik>`_ (legacy) by Raphael Jasjukaitis `jasjukaitis <https://github.com/jasjukaitis>`_.

`django-piwik` is metioned as an official Django plugin for Matomo: https://matomo.org/integrate/

Requirements
------------

* Django


Installation
------------

Using PyPI you can simply type into a terminal:

``pip install django-matomo``

or

``easy_install django-matomo``


Configuration
-------------

Add ``matomo`` to the list of ``INSTALLED_APPS`` in your ``settings.py`` file.

Also ``MATOMO_SITE_ID`` (e.g. `51`) and ``MATOMO_URL`` (e.g. ``'http://matomo.example.com/'``, please don't forget the trailing slash!) are required.


In the template, put ``{% load matomo_tags %}`` to the top and add ``{% tracking_code %}`` before the ``</body>`` tag.

That's it. Happy tracking!

Uploading to PyPi
-----------------

Article on Medium (Towards Data Science) on `how to upload packages to PyPi <https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3>`_.

In short:

``python setup.py sdist``

``twine upload dist/*``

Version history
---------------

* Main changes were introduced in ``0.1`` version of the package.

* Versions up to ``0.1.4`` are mainly formatting changes for the RST README format.

* Version ``0.1.5`` information on uploading to PyPi added to the README. Minor formatting changes.


Author(s)
---------

Copyright 2022 Mikolaj Buchwald <mikolaj.buchwald@gmail.com>

as `django-piwik`: Copyright 2013 Raphael Jasjukaitis <webmaster@raphaa.de>


Released under the BSD license.