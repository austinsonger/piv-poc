"""
ASGI config for src project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

if env.APP_ENVIRONMENT == "development":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.development")
else:
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.production")


application = get_asgi_application()
