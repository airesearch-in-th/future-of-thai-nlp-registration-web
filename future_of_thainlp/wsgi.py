"""
WSGI config for future_of_thainlp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import dotenv
import os

from django.core.wsgi import get_wsgi_application

# Select and read environment variables from .env file
dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env' if os.environ.get('DJANGO_ENV', '').lower() == 'production' else '.env.debug'), override=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'future_of_thainlp.settings')

application = get_wsgi_application()
