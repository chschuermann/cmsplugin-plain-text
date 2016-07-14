====================
cmsplugin-plain-text
====================

|pypi| |ci|

.. |pypi| image:: https://badge.fury.io/py/cmsplugin-plain-text.png
    :target: https://badge.fury.io/py/cmsplugin-plain-text
    :alt: Latest Version

.. |ci| image:: https://travis-ci.org/chschuermann/cmsplugin-plain-text.png?branch=master
    :target: https://travis-ci.org/chschuermann/cmsplugin-plain-text
    :alt: Development Status

A simple plaintext plugin for django CMS.

Requirements
------------

- ``Django`` >= 1.5
- ``django-cms`` >= 3.0

Quickstart
----------

Installation::

    $ pip install cmsplugin-plain-text

Configure installed apps in your ``settings.py`` ::

    INSTALLED_APPS = (
        ...,
        'cmsplugin_plain_text',
    )

Migrate your database ::

    $ ./manage.py migrate cmsplugin_plain_text

If you are using Django < 1.7 in conjunction with South, make sure your SOUTH_MIGRATION_MODULES setting contains this
line.::

    SOUTH_MIGRATION_MODULES = {
        ...,
        'cmsplugin_plain_text': 'cmsplugin_plain_text.south_migrations',
    }

Running Tests
-------------
::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
