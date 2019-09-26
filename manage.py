#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import dotenv
import os
import sys


def main():
    # Select and read environment variables from .env file
    dotenv.read_dotenv(os.path.join(os.path.dirname(__file__), '.env' if
        os.environ.get('DJANGO_ENV', '').lower() == 'production' else '.env.debug'), override=True)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'future_of_thainlp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
