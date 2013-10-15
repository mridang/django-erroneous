import sys
from setuptools import setup, find_packages

setup(
    name = "django-erroneous",
    package_data = {
        'erroneous': [
            'README.rst',
            'LICENSE.txt',
            'erroneous.templates',
        ],
    },
    author = "Mridang Agarwalla",
    author_email = "mridang.agarwalla@gmail.com",
    download_url='http://github.com/mridang/django-erroneous/downloads',
    description = "django-erroneous makes it easy to collect and log Django application errors.",
    url = "http://github.org/mridang/django-erroneous",
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    packages = [
        'erroneous',
        'erroneous.migrations',
    ],
    zip_safe = False,
    license = "BSD License",
    install_requires = [
        'Django>=1.4',
        'South>=0.7.2'
    ],
    version = '0.2.0',
)