import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'EyELAK97Jpqyba3FJbySdRfssp8rf7pp4264165'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '157.230.226.52', ]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': ',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': 'localhost'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'readb',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': 'localhost'
    }
}

# Email
EMAIL_HOST = 'mail.realestateappdjango.com'
EMAIL_PORT = 26
EMAIL_HOST_USER = 'noreply@realestateappdjango.com'
EMAIL_HOST_PASSWORD = 'kVNUtBTaIQRQ4M'
