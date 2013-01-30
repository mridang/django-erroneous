============
django-erroneous
============

View all Django errors from right within the administration console.

Erroneous traps Django's in-built exception signal, captures the traceback . which would be the same beautiful exception page that Django displays when debugging is enabled . and saves it to the database so you can view it later.

It's quite similar to django-sentry from the folks at Disqus but a more lightweight, no-frills, error-logging system for Django. Credits to David Cramer over at Disqus for the initial django-db-log which is the work this is based upon.

If there's a feature that you're missing and you'd like added, please create an issue on the project page at Github or create the fix yourself and send me a pull request. Adding a few small features here and there are okay but this is in no way aimed to encompass all the functionality of a full-blown error-logging stack like Sentry.

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

There isn't much else than that to get it up and running.

Future
------

* support for logging to other sinks: message queues, non-relational databases.

