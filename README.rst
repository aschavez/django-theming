Django Theming
**************

.. image:: https://pypip.in/v/django-theming/badge.svg?text=version&style=flat
    :target: https://pypi.python.org/pypi/django-theming

.. image:: https://pypip.in/d/django-theming/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/django-theming

.. image:: https://pypip.in/py_versions/django-theming/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/django-theming

.. image:: https://pypip.in/status/django-theming/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/django-theming
    
.. image:: https://pypip.in/license/django-theming/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/django-theming

Django application, implement theming concept, flexible and configurable. Allow theming for host url.

Installation
============

You can install the most recent **Django Theming** version using pip: ::

    pip install django-theming

Setup
=====

**NOTE**: The following settings should be added to the project file `settings.py`.

1. Add 'theming' to ``INSTALLED_APPS``: ::

    INSTALLED_APPS += ( 'theming', )

2. Add 'theming.middleware.ThemingMiddleware' to ``MIDDLEWARE_CLASSES``: ::

    MIDDLEWARE_CLASSES += ( 'theming.middleware.ThemingMiddleware', )

2. Add 'theming.loaders.ThemeLoader' to ``TEMPLATE_LOADERS``: ::

    TEMPLATE_LOADERS += ( 'theming.loaders.ThemeLoader', )

4. Declare ``THEME_ROOT`` and ``MEDIA_ROOT``: ::

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    
    THEME_ROOT = os.path.join(BASE_DIR, 'themes')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

5. Declare ``MEDIA_URL``: ::

    MEDIA_URL = '/media/'

6. Declare ``THEME_MEDIA_ROOT`` y ``THEME_MEDIA_URL``: ::

    THEME_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'themes')
    THEME_MEDIA_URL = os.path.join(MEDIA_URL, 'themes')

7. Declare host/theme config tuple ``THEME_CONFIG``: ::

    THEME_CONFIG = (
        (r'^(.+\.)?dominio\.pe', 'default'),
        (r'^(.+\.)?test\.pe', 'test'),
    )

Usage
=====

It should create a folder ``themes`` at the project with the following structure: ::

    project_django/
    | -- themes/
        | -- default/  ** theme name
            | -- templates/
            | -- media/
            |   | -- styles/
            |   | -- scripts/
            |   | -- images/
            | -- metadata.json

**NOTE**: We use ``media`` instead of ``static`` for independent assets by theme.

In the file ``metadata.json`` it should include information on the theme: ::

    {
        "slug": "default",
        "name": "Default",
        "description": "Theme Default",
        "author": "Author",
        "version": "1.0"
    }

You can use the template tag ``theme`` to refer to the theme assets as follows: ::

    <link rel="stylesheet" href="{% theme 'styles/main.css' %}" />

**NOTE**: The tamplate tag ``theme`` will refer to the ``media/themes/<theme_name>`` folder, if not find the file in that path, it will search in ``static/``

You can use the command ``collectthemes`` to copy all assets of the theme to the location  ``media/``: ::

    python manage.py collectthemes
    
    options:
    - l, --link : Create a symbolic link to each file instead of copying.
    - f, --force: Force to overwrite content.

Contributing
============

Development of **django-theming** happens at github: https://github.com/achavezu89/django-theming

Credits
=======

* Andres Chavez: https://github.com/achavezu89
* Giorgio Leveroni: https://github.com/ppold
* Antonio Ognio: https://github.com/gnrfan
* Antonio Kobashikawa: https://github.com/akobashikawa
