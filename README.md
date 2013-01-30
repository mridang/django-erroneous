============
django-erroneous
============

``django-erroneous`` is a tool for improving your Django error logging.

Features
--------

* A simple user interface for browsing error records in the database.

Installation
------------

Start with Django 1.3 or higher; erroneous is intended for use with the new logging
configuration first available in that version.

To install, simply run::

    pip install django-erroneous

Configuration
-------------

1. Add ``erroneous`` to your ``INSTALLED_APPS`` setting.

2. Run ``manage.py migrate`` to create the database tables, or if you're really
   logging to a second database and have disabled South migrations for erroneous,
   run ``manage.py syncdb``.

The last two steps can be skipped if you don't want the UI.

Future
------

* support for logging to other sinks: message queues, non-relational databases.

