# -*- coding: utf-8 -*-
'''
Production Configurations

- Use djangosecure
- Use Amazon's S3 for storing static files and uploaded media
- Use sendgrid to send emails
- Use MEMCACHIER on Heroku
'''
from configurations import values

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
try:
    from S3 import CallingFormat
    AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
except ImportError:
    # TODO: Fix this where even if in Dev this class is called.
    pass

from .common import Common


class Production(Common):

    DEBUG = True
    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # SECRET KEY
    SECRET_KEY = "Change me" # values.SecretValue()
    # END SECRET KEY

    # django-secure
#    INSTALLED_APPS += ("djangosecure", )

    # set this to 60 seconds and then to 518400 when you can prove it works
#    SECURE_HSTS_SECONDS = 60
#    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
#    SECURE_FRAME_DENY = values.BooleanValue(True)
#    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
#    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
#    SESSION_COOKIE_SECURE = values.BooleanValue(False)
#    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
#    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    # end django-secure

    # SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    # END SITE CONFIGURATION

    INSTALLED_APPS += ("gunicorn", )

    # CACHING
    # Only do this here because thanks to django-pylibmc-sasl and pylibmc
    # memcacheify is painful to install on windows.
    try:
        # See: https://github.com/rdegges/django-heroku-memcacheify
        from memcacheify import memcacheify
        CACHES = memcacheify()
    except ImportError:
        CACHES = values.CacheURLValue(default="memcached://127.0.0.1:11211")
    # END CACHING

    # Your production stuff: Below this line define 3rd party library settings
