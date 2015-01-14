from setuptools import setup
from codecs import open
from os import path

BASE = path.abspath(path.dirname(__file__))

with open(path.join(BASE, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-theming',
    version='1.0',
    url='https://github.com/achavezu89/django-theming',
    author='Andres Chavez',
    author_email='achavezu89@gmail.com',
    description=('Django application, implement theming concept, '
                 'flexible and configurable. Allow theming for host url.'),
    license='GPL',
    packages=[
        'theming',
        'theming.management',
        'theming.management.commands',
        'theming.templatetags'
    ],
    include_package_data=True,
    long_description = long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='django theme template host',
)