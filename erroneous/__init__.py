from django.core.signals import got_request_exception
from django.conf import settings

from erroneous.signals import LoggingExceptionHandler

if not settings.DEBUG: 
    got_request_exception.connect(LoggingExceptionHandler.create_from_exception)