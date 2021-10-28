from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xw0m+o%z&v-bv8at+7be#)p((a_&e8=1vd#xy+xy17gykt17&f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# SQLITE
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR + '/db.sqlite3',
#     }
# }

# MYSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.mysql',
#         'NAME': 'aca',
#         'USER': 'postgres',
#         'PASSWORD': 'CLAVEMAESTRA',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         # 'OPTIONS': {
#         #     'sql_mode': 'traditional',
#         # }
#     }
# }

#POSTGRESQL
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': 'curso-django',

        'USER': 'postgres',

        'PASSWORD': 'CLAVEMAESTRA',

        'HOST': '127.0.0.1', #'localhost'

        'PORT': '5432',

    }

}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), 'static'),
)