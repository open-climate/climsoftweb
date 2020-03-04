"""
Local settings are only used when developing the software locally using `./manage.py runserver`. E.g.

    ./manage.py runserver 127.0.0.1:8080 --settings=climsoftweb.settings.local

or

    export DJANGO_SETTINGS_MODULE="climsoftweb.settings.local"
    ./manage.py runserver 127.0.0.1:8080

..note::

   If using MySQL you must also set the DJANGO_DB_USER and mysql_instance_password environment variables.

"""
import os

from climsoftweb.settings.base import *


CONNECT_MYSQL = False

INSPECT_DB = False


DEBUG = True

ALLOWED_HOSTS = ['*']

CUSTOM_BTN = 'btn-info'

SETTINGS_EXPORT = ['CUSTOM_BTN']


if CONNECT_MYSQL:
    # Example call for inspectdb:
    # /webapps/climsoftweb/bin/python3 manage.py inspectdb --settings=climsoftweb.settings.local > climsoft_models.py
    #
    # Example call for migrate:
    # /webapps/climsoftweb/bin/python3 manage.py migrate --settings=climsoftweb.settings.local
    import pymysql
    # https://stackoverflow.com/a/59591269/
    pymysql.version_info = (1, 3, 13, "final", 0)
    pymysql.install_as_MySQLdb()

    SECONDARY_DB_NAME = 'default' if INSPECT_DB else 'climsoft'

    DATABASES[SECONDARY_DB_NAME] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mariadb_climsoft_test_db_v4', # os.getenv('DJANGO_DB_NAME'),
        'USER': os.getenv('DJANGO_DB_USER'),
        'PASSWORD': os.getenv('mysql_instance_password'),
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }


# INSTALLED_APPS += ('debug_toolbar',)
#
# MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
#
# # The Django Debug Toolbar will only be shown to these client IPs.
# INTERNAL_IPS = (
#     '127.0.0.1',
# )
#
# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
#     'SHOW_TEMPLATE_CONTEXT': True,
#     'HIDE_DJANGO_SQL': False,
# }
