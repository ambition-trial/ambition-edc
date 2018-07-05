from ambition_sites import fqdn

from ..base import *
from ..logging import LOGGING

DEBUG = False

# WARNING_MESSAGE = 'This is a test system. Do not use for production data collection! '

FQDN = fqdn

ETC_DIR = os.path.join('/etc', APP_NAME, 'uat')

RANDOMIZATION_LIST_PATH = os.path.join(ETC_DIR, 'test_randomization_list.csv')

KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')
AUTO_CREATE_KEYS = False

SECRET_KEY = '2^p0phb&x&ntbsduf6afw(@efi(+!&hm_lrjr-+$5v(t0_f+6t'

INDEX_PAGE = f'https://{FQDN}'

CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

STATIC_ROOT = '/var/www/ambition/uat/static'

CUPS_SERVERS = {
    'bhp.printers.bhp.org.bw': 'bhp.printers.bhp.org.bw',
    'localhost': None}

# django_offline / django_offline files
EDC_SYNC_SERVER_IP = None
DJANGO_OFFLINE_FILES_REMOTE_HOST = None
DJANGO_OFFLINE_FILES_USER = None
DJANGO_OFFLINE_FILES_USB_VOLUME = None
