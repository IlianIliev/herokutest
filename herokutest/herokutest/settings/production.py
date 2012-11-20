import dj_database_url

from herokutest.settings import *


# PRODUCTION SPECIFIC SETTINGS GOES HERE
DEBUG = TEMPLATE_DEBUG = False

DATABASES['default'] =  dj_database_url.config()
