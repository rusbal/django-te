from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True

TEST_RUNNER = "discover_runner.DiscoverRunner"
TEST_DISCOVERY_ROOT = PROJECT_DIR + '/tests'
