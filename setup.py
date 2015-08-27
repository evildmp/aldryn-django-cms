# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_cms import __version__

setup(
    name="aldryn-cms",
    version=__version__,
    description='An opinionated django CMS setup bundled as an Aldryn Addon',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-cms',
    packages=find_packages(),
    install_requires=(
        'aldryn-addons',
        'django-cms==3.1.2',
        'django-reversion',
        # common
        # TODO: mostly to be split out into other packages
        'django-compressor',
        'YURL',
        'South',
        'requests',
        'Pillow',
        'lxml',
        'django-treebeard',
        'django-simple-captcha',
        'BeautifulSoup',
        'django-parler',
        'django-robots',
        'aldryn-boilerplates',
        'django-filer',
        'django-hvad',
        'aldryn-snake',

        # default plugins
        # TODO: split into other packages
        'djangocms-googlemap',
        'djangocms-link',
        'djangocms-snippet',
        'djangocms-text-ckeditor',
        'cmsplugin-filer',
    ),
    include_package_data=True,
    zip_safe=False,
)
