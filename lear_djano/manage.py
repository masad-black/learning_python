#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.

manage.py: is like a CEO of the companey, it wii jsut give the orders and thing will happen
most of things are run from here like, app creation, migration, admin, run server and other things!!
"""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
