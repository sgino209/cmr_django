# (c) Shahar Gino, April-2018, sgino209@gmail.com
#
# WSGI config for Motzkin project.
# It exposes the WSGI callable as a module-level variable named ``application``.

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Motzkin.settings")

application = get_wsgi_application()

#Add static serving using whitenoise
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
